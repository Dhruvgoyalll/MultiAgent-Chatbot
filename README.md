# MultiAgent-Chatbot
# 🤖 Multi-Agent Chatbot with Groq, OpenAI, LangChain, and FastAPI

This project is a powerful **Multi-Agent Chatbot System** that leverages the combined capabilities of **Groq’s blazing-fast inference engine**, **OpenAI's GPT-4o**, and **LangChain’s orchestration framework** to create intelligent and dynamic conversations between multiple agents. Built with **FastAPI** as the backend and **Streamlit** for the front-end interface, this chatbot demonstrates how multiple LLM-powered agents can collaborate in real-time to reason, debate, and solve complex queries efficiently. The system is designed using **LangGraph** to manage agent state and flow, while the **Tavily Search API** augments responses with accurate, up-to-date web results, making the conversations more informed and grounded in current facts.

The FastAPI server is deployed seamlessly using **Render**, and the interactive demo UI is built using **Streamlit**, allowing users to easily interact with the agents from any device. This chatbot showcases the true potential of **multi-agent LLM systems**—where different agents with distinct roles (e.g., a researcher, a summarizer, a coder, and a decision-maker) collaborate to solve tasks more effectively than a single model operating alone.

---

### 🚀 Live Demo

[🌐 Click here to try the Multi-Agent Chatbot](https://multiagent-chatbot-ollama.streamlit.app/)

---

## 🔑 Tech Stack

- **LangChain** – For orchestrating the logic and flow between multiple agents and tools  
- **LangGraph** – For managing graph-based state transitions between agents  
- **Groq (LLaMA 3)** – Lightning-fast LLaMA 3 inference through Groq API  
- **OpenAI GPT-4o** – Powerful language understanding and reasoning model  
- **Tavily Search API** – For real-time, accurate web search to assist agents  
- **FastAPI** – High-performance API backend for serving agent responses  
- **Streamlit** – Lightweight, interactive frontend for users to chat with agents  
- **Python** – The core language powering the logic, integration, and execution  

---

## 📁 Project Structure

```bash
multiagent-chatbot/
│
├── agents/              # Definitions for different agents and their roles
├── chains/              # LangChain & LangGraph chains configuration
├── api/                 # FastAPI routes and backend logic
├── streamlit_app/       # Frontend UI using Streamlit
├── utils/               # Utility functions for parsing, context management, etc.
├── main.py              # FastAPI app entrypoint
├── requirements.txt     # Dependencies
└── README.md            # This file

