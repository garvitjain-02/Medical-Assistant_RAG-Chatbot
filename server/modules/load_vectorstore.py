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
