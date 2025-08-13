import requests
from config import API_URL

def upload_pdfs_api(files):
    files_payload=[("files", (f.name, f.read(), "application/pdf")) for f in files]
    return requests.post(f"{API_URL}/upload_pdfs/", files=files_payload)

def ask_questions_api(question):
    payload = {"question": question}
    return requests.post(f"{API_URL}/ask_questions/",data=payload) 