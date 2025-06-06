from app.pdf_parser import get_all_pdfs, parse_pdf
from app.embed_store import add_chunks_to_store

def index_pdfs():
    print("📄 Ingesting all PDFs in /data...")
    pdf_files = get_all_pdfs()
    total_chunks = 0
    for pdf_path in pdf_files:
        chunks = parse_pdf(pdf_path)
        add_chunks_to_store(chunks)
        total_chunks += len(chunks)
    print(f"✅ Indexing completed. Total chunks processed: {total_chunks}")

if __name__ == "__main__":
    index_pdfs()
