import gradio as gr
import requests
from fastapi import FastAPI

# The address of your local Ollama engine
LOCAL_OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

def generate_text(prompt: str):
    if not prompt: 
        return "Please enter a prompt."
    
    try:
        # Prepare the request for the gemma:2b model (optimized for lower RAM)
        data = { 
            "model": "gemma:2b", 
            "prompt": prompt, 
            "stream": False 
        }
        
        # Send to local API
        response = requests.post(LOCAL_OLLAMA_ENDPOINT, json=data, timeout=60)
        response.raise_for_status()
        
        return response.json().get("response", "No response found.")
        
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create the Gradio Interface
gui = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=5, label="Enter your coding question", placeholder="e.g., Write a Python function for a binary search..."),
    outputs=gr.Textbox(label="Assistant Output"),
    title="Amr's Local Coding Assistant 🤖",
    description="Lab 5: Serving Open-Source LLMs locally with Ollama (Optimized with Gemma 2B)."
)

# Mount Gradio into FastAPI
app = FastAPI(title="MLOps Local API")
app = gr.mount_gradio_app(app, gui, path="/")