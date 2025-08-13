from fastapi import APIRouter,UploadFile,File
from typing import List
from modules.load_vectorstore import load_vectorstore
from fastapi.responses import JSONResponse
from logger import logger

router = APIRouter()
@router.post("/upload_pdf")
async def upload_pdf(files: List[UploadFile] = File(...)):
    try:
        logger.info("Received uploaded files")
        load_vectorstore(files)
        logger.info("Added document to vectorstore")
        return {"messages":"files processed and vector store updated"}

    except Exception as e:
        logger.exception("Error uploading PDF files")
        return JSONResponse(status_code=500, content={"message": "Error processing PDF files"})