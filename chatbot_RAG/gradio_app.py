import gradio as gr
from app.pdf_parser import get_all_pdfs, parse_pdf
from app.embed_store import add_chunks_to_store
from app.retriever import retrieve_relevant_chunks
from app.groq_llm import generate_answer

# Ingest PDFs once at startup
def ingest_documents():
    print("📥 Ingesting PDFs...")
    pdf_files = get_all_pdfs()
    for pdf_path in pdf_files:
        chunks = parse_pdf(pdf_path)
        add_chunks_to_store(chunks)
    print("✅ Ingestion complete.")

def chatbot_interface(query):
    if not query.strip():
        return "❗ Please enter a question."

    chunks = retrieve_relevant_chunks(query)

    if not chunks:
        return "🤔 No relevant information found."

    answer = generate_answer(query, chunks)

    # Show both source file and page number
    sources = set()
    for c in chunks:
        meta = c.get("metadata", {})
        source = meta.get("source", "Unknown")
        page = meta.get("page", "?")
        sources.add(f"📄 [Page {page}]({source})")

    source_links = "\n".join(sources)

    return f"**Answer:**\n{answer}\n\n---\n**Sources:**\n{source_links}"

# Run ingestion once before launching UI
ingest_documents()

gr.Interface(
    fn=chatbot_interface,
    inputs=gr.Textbox(label="Ask a question about HR policies"),
    outputs=gr.Markdown(label="Answer"),
    title="🧠 HR Policy Chatbot",
    description="Ask me anything about HR policies. I’ll answer from PDF data and show sources.",
    allow_flagging="never",
).launch()
