from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware

app = FastAPI(title="Medical Assistant RAG Chatbot",description="API for a chatbot that provides medical assistance using RAG (Retrieval-Augmented Generation) techniques.")

#CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#middleware exception handlers
app.middleware("http")(catch_exception_middleware)

#routers

# 1. uploadpdf


# 2. askquestions