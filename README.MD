# 📊 FinInsight AI

**Enterprise Financial Document Intelligence using RAG + Groq + FastAPI + Streamlit**

FinInsight AI is a Retrieval-Augmented Generation (RAG) application that enables users to upload financial PDF documents and ask natural language questions. The system retrieves relevant information from the uploaded document using semantic search and generates accurate answers using Groq's Llama model.

---

# 🚀 Features

* 📄 Upload Financial PDF Documents
* 🔍 Automatic PDF Text Extraction
* ✂️ Intelligent Text Chunking
* 🧠 Semantic Embeddings
* 📚 ChromaDB Vector Database
* 🤖 Groq Llama 3.3 Large Language Model
* 💬 Chat Interface using Streamlit
* 📑 Source Page References
* ⚡ FastAPI Backend

---

# 🏗 Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### AI

* Groq (Llama 3.3 70B Versatile)

### Vector Database

* ChromaDB

### Embedding Model

* Sentence Transformers
* all-MiniLM-L6-v2

### PDF Processing

* PyMuPDF

---

# 📁 Project Structure

```
FinInsight/

│
├── backend/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── uploads/
│   ├── chroma_db/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── api.py
│   ├── components.py
│   └── styles.py
│
├── .env
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>

cd FinInsight
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

If needed install Streamlit separately

```bash
pip install streamlit requests
```

---

# 🔑 Configure Environment Variables

Create a `.env` file in the project root.

Example

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# 🔑 Get a Groq API Key

1. Visit

https://console.groq.com

2. Login

3. Create an API Key

4. Copy it into the `.env` file

---

# ▶️ Run Backend

Open Terminal 1

```bash
cd backend

python -m uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

Open Terminal 2

```bash
cd frontend

python -m streamlit run app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 📄 How to Use

1. Start Backend
2. Start Frontend
3. Upload a PDF
4. Wait until indexing completes
5. Ask questions in natural language

Examples

* What is this document about?
* Summarize the report.
* What is the total revenue?
* What are the risk factors?
* What are the company's future plans?
* Explain the cash flow statement.

---

# 📌 API Endpoints

### Upload PDF

```
POST /upload/
```

Uploads and indexes a PDF.

---

### Ask Questions

```
POST /query/
```

Example Request

```json
{
    "question": "What is this PDF about?"
}
```

---

# 📷 Demo Workflow

```
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Chunk Text
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
Semantic Search
      │
      ▼
Groq Llama
      │
      ▼
Generate Answer
```

---

# 🧹 Reset Vector Database

To remove previous indexed documents

1. Stop the backend

2. Delete

```
backend/chroma_db/
```

3. Restart the backend

4. Upload a new PDF

---

# 📦 Requirements

* Python 3.11+
* Groq API Key
* Internet Connection
* 8 GB RAM Recommended

---

# 👨‍💻 Author

**Vishal Sable**

B.Tech Artificial Intelligence & Data Science

---

# 📄 License

This project is developed for educational and hackathon purposes.
