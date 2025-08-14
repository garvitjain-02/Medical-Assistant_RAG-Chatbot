# ⚕️ Medical Assistant RAG Chatbot

A sophisticated medical document assistant powered by Retrieval-Augmented Generation (RAG) that helps users understand medical documents and answer health-related questions using AI.

## 🚀 Features

- **📄 PDF Document Upload**: Upload medical documents in PDF format for analysis
- **🤖 AI-Powered Chat**: Interactive chat interface with medical document context
- **🔍 Smart Document Retrieval**: Advanced vector search using Pinecone and Google AI embeddings
- **📚 Source Attribution**: View source documents for each answer
- **💾 Chat History**: Download conversation history for record-keeping
- **🛡️ Medical Safety**: Built-in safeguards to prevent medical advice/diagnosis
- **⚡ Fast Response**: Powered by Groq's Llama3-70B model for quick responses

## 🏗️ Architecture

This project follows a client-server architecture:

### Frontend (Client)
- **Framework**: Streamlit
- **Components**:
  - Chat Interface (`chatUI.py`)
  - Document Upload (`upload.py`)
  - History Download (`history_download.py`)
  - API Integration (`api.py`)

### Backend (Server)
- **Framework**: FastAPI
- **AI/ML Stack**:
  - **LLM**: Groq (Llama3-70B-8192)
  - **Embeddings**: Google Generative AI
  - **Vector Database**: Pinecone
  - **Document Processing**: LangChain + PyPDF
- **Modules**:
  - LLM Chain Management (`llm.py`)
  - Vector Store Operations (`load_vectorstore.py`)
  - Query Processing (`query_handler.py`)
  - PDF Handling (`pdf_handler.py`)

## 📋 Prerequisites

- Python 3.8+
- API Keys for:
  - [Groq](https://console.groq.com/) (for LLM)
  - [Google AI](https://makersuite.google.com/app/apikey) (for embeddings)
  - [Pinecone](https://app.pinecone.io/) (for vector database)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/garvitjain-02/Medical-Assistant_RAG-Chatbot.git
   cd Medical-Assistant_RAG-Chatbot
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install server dependencies**
   ```bash
   cd server
   pip install -r requirements.txt
   ```

4. **Install client dependencies**
   ```bash
   cd ../client
   pip install -r requirements.txt
   ```

5. **Environment Setup**
   
   Create a `.env` file in the `server` directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   PINECONE_INDEX_NAME=medicalindex
   ```

## 🚀 Running the Application

### Start the Backend Server

1. Navigate to the server directory:
   ```bash
   cd server
   ```

2. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at `http://localhost:8000`

### Start the Frontend Client

1. In a new terminal, navigate to the client directory:
   ```bash
   cd client
   ```

2. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

   The web interface will be available at `http://localhost:8501`

## 📖 Usage

1. **Upload Documents**: Use the sidebar to upload medical PDF documents
2. **Ask Questions**: Type your medical questions in the chat interface
3. **View Sources**: Each answer includes references to source documents
4. **Download History**: Save your conversation history for future reference

## 🔧 API Endpoints

- `POST /upload/` - Upload PDF documents
- `POST /ask/` - Ask questions and get AI responses

## 🛡️ Safety Features

- **No Medical Advice**: The system explicitly states it does not provide medical advice or diagnoses
- **Context-Based Responses**: Answers are based only on uploaded documents
- **Source Attribution**: All responses include source document references
- **Professional Tone**: Maintains a calm, factual, and respectful communication style

## 🏥 Use Cases

- **Medical Research**: Analyze medical papers and research documents
- **Patient Education**: Help patients understand medical reports and documents
- **Healthcare Training**: Assist medical students and professionals with document analysis
- **Clinical Documentation**: Process and query clinical notes and reports

## 🔍 Technical Details

- **Document Processing**: PDFs are split into 500-character chunks with 100-character overlap
- **Vector Search**: Uses Pinecone for similarity search with top-3 document retrieval
- **Embedding Model**: Google's `models/embedding-001` for document vectorization
- **Response Generation**: Groq's Llama3-70B model with custom medical assistant prompt

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
<!-- 
## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details. -->

## ⚠️ Disclaimer

This application is designed for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.

## 🆘 Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Built with ❤️ for the medical community**
