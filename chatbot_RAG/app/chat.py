from app.pdf_parser import get_all_pdfs, parse_pdf
from app.embed_store import add_chunks_to_store
from app.retriever import retrieve_relevant_chunks
from app.groq_llm import generate_answer

def ingest_documents():
    print("📥 Ingesting PDFs...")
    pdf_files = get_all_pdfs()
    for pdf_path in pdf_files:
        chunks = parse_pdf(pdf_path)
        add_chunks_to_store(chunks)

def chat():
    print("\n🤖 HR Policy Chatbot (Ask a question or type 'exit')\n")

    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"):
            break

        relevant_chunks = retrieve_relevant_chunks(query)
        answer = generate_answer(query, relevant_chunks)

        print("\nAnswer:\n", answer)
        print("\nSources:")
        for c in relevant_chunks:
            print(f"🔗 {c['source']}")
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    ingest_documents()
    chat()
