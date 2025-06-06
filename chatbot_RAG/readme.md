# 🧠 HR Policy Chatbot (RAG + Groq)

A Retrieval-Augmented Generation (RAG) chatbot that answers employee questions about HR policies using information extracted from PDFs. It uses Groq's LLaMA-3 model for language generation and ChromaDB for persistent, semantic search.

---

## 🚀 Features

- 🔍 Semantic search over PDF-based HR policies
- 💬 Answer generation using Groq’s LLaMA-3
- 📄 Source links for transparency and traceability
- 🔁 Incremental PDF ingestion with deduplication
- 💾 Persistent vector storage using Chroma
- 🖼️ Gradio web interface for ease of use
- 🧑‍💻 CLI mode for terminal-based access

---

### 📦 Installation

Install dependencies:

bash
pip install -r requirements.txt

---

## ▶️ How to Use

### 📥 Add Your PDFs

- Place your HR policy PDFs inside the `data/` folder.
- On the first run, the chatbot will:
  - Parse and chunk the PDFs
  - Generate embeddings
  - Deduplicate content using chunk-level hashing
  - Persist data into ChromaDB
- Subsequent runs will only ingest **new or updated PDFs**.

---

### 🧪 CLI Mode

bash
python main.py

---

## 🔧 Tech Stack

| Layer         | Tool/Library                          |
|---------------|----------------------------------------|
| LLM           | [Groq API](https://console.groq.com/) - LLaMA 3 |
| Embeddings    | [SentenceTransformers](https://www.sbert.net/) - `all-MiniLM-L6-v2` |
| Vector Store  | [ChromaDB](https://www.trychroma.com/) with persistence |
| PDF Parsing   | [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) |
| UI Interface  | [Gradio](https://www.gradio.app/) for web app |
| Programming   | Python 3.9+ |
| Deployment    | Local (future: Azure stack + OpenAI) |

---

## 🔮 Future Enhancements

- 📊 **Table & Image Support**: Parse and understand complex data like tables and visuals from PDFs.
- 🌍 **Multilingual Support**: Enable understanding of documents and queries in multiple languages.
- 🔁 **Reinforcement Learning (RLAIF)**: Improve accuracy based on user feedback over time.
- ☁️ **Azure Deployment**:
  - Azure Blob Storage for PDF hosting
  - Azure Cognitive Search for hybrid indexing
  - Azure OpenAI for LLM inference
  - Azure App Service for frontend hosting
- 📦 **Dockerization** for containerized deployment
- 🔐 **User Authentication** and session history tracking

