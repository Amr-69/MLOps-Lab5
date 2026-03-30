# Amr's Local AI Coding Assistant - MLOps Lab 5 🤖

This repository contains a local LLM deployment for **Lab 5: Serving Open-Source LLMs locally with Ollama**. The application provides a web-based chat interface to interact with a specialized coding assistant.

## 🛠️ Tech Stack
- **Engine:** [Ollama](https://ollama.com/) (Local LLM Runtime)
- **Model:** `gemma:2b` (Optimized for local performance)
- **Backend:** FastAPI (Python)
- **Frontend:** Gradio (Web UI)
- **Server:** Uvicorn

## 🚀 Optimization Logic
Originally, the project was intended to run `codellama:7b-instruct`. However, due to local system constraints (approx. 2.0 GiB available RAM), the deployment was optimized by pivoting to the **Gemma 2B** model. 

This model swap resolved **Out of Memory (OOM)** errors while maintaining functional logic for common coding tasks like Binary Search and Python function generation.

## ⚙️ Setup Instructions

### 1. Install & Pull Model
Ensure Ollama is installed and running, then pull the required model:
```powershell
ollama pull gemma:2b