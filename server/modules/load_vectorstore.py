import os
import time
from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm
from pinecone import Pinecone, ServerlessSpec
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
PINECONE_ENV="us-east-1"
PINECONE_INDEX_NAME="medicalindex"

os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY

UPLOAD_DIR="./uploaded_docs"
os.makedirs(UPLOAD_DIR,exist_ok=True)

#create pinecone instance
pc = Pinecone(api_key=PINECONE_API_KEY)
spec = ServerlessSpec(
    cloud="aws",
    region=PINECONE_ENV
)
existing_indexes=[i["name"] for i in pc.list_indexes()]

if PINECONE_INDEX_NAME not in existing_indexes:
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=768,
        metric="dotproduct",
        spec=spec
    )
    while not pc.describe_index(PINECONE_INDEX_NAME).status["ready"]:
        time.sleep(1)


index = pc.Index(PINECONE_INDEX_NAME)

# load,split,embed and upsert pdf docs content

def load_vectorstore(uploadedfiles):
    embed_model = GoogleGenerativeAIEmbeddings(model="models/embedding-003")
    file_path=[]

    # 1. upload 
    for file in uploadedfiles:
        save_path=Path(UPLOAD_DIR)/file.file_name
        with open(save_path, "wb") as f:
            f.write(file.file.read())

        file_path.append(str(save_path))

    # 2. split

    for file in file_path:
        loader=PyPDFLoader(file)
        documents=loader.load()

        splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks=splitter.split_documents(documents)

        text = [chunk.page_content for chunk in chunks]
        metadata = [chunk.metadata for chunk in chunks]
        ids = [f"{Path(file).stem}--{i}" for i in range(len(chunks))]

        # 3. Embedding
        print(f"Embedding {len(chunks)} Chunks")
        embedding = embed_model.embed_documents(text)

        # 4. Upsert in Pinecone
        print(f"Upserting Embeddings")
        with tqdm(total=len(embedding), desc="Upserting to pinecone") as progress:
            index.upsert(vectors=zip(ids,embedding,metadata))
            progress.update(len(embedding))


        print(f"Finished Upserting {len(embedding)} Embeddings")
        print(f"Upload complete for {file}")