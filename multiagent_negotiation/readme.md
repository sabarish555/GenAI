# 🤖 AI-Powered Procurement Negotiation Assistant with LangChain and Ollama

This project builds an **AI negotiation assistant** using [LangChain](https://www.langchain.com/), [Ollama](https://ollama.com/), and **LLaMA 3** running locally. It simulates a multi-step procurement process where an LLM agent analyzes a **tender document**, **product brief**, **supplier performance data**, and **vendor bids** to generate a **negotiation strategy** and draft a **professional email** to suppliers.

---

## 💡 Key Features

- 🧾 **Tender Summary Agent** – Summarizes lengthy tender documents in bullet points.
- 📦 **Product Brief Agent** – Condenses product details for procurement teams.
- 📊 **Negotiation Strategy Agent** – Analyzes supplier performance + bids and generates strategy.
- ✉️ **Email Drafting Agent** – Crafts negotiation emails based on the strategy.

---

## 🧠 Tech Stack

- 🦜 [LangChain](https://www.langchain.com/)
- 🦙 [Ollama](https://ollama.com/) with `llama3:latest`
- 📁 JSON & TXT file handling
- 🐍 Python 3.10+

---

## ⚙️ How It Works

1. Reads input files:
   - `tender_001.txt`
   - `product_brief_001.txt`
   - `supplier_perf.json`
   - `bids.json`

2. Agents process each input using prompt templates and LLM chains.

3. Final output includes:
   - 📄 Tender summary
   - 📦 Product summary
   - 🧠 Negotiation recommendations
   - ✉️ Draft negotiation email

---

## 🚀 Getting Started

1. Install dependencies:
   ```bash
   pip install langchain langchain-community
keywrods: LangChain project, Procurement AI, LangChain negotiation agent, LangChain tender summary, Ollama llama3 LangChain, LangChain local LLM, LangChain email generation, Python procurement AI, LangChain ChatOllama, B2B AI automation, AI negotiation bot, LangChain multi-agent, RFP summary agent, supplier negotiation assistant, AI for sourcing and procurement
