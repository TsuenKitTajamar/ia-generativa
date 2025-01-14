import re
import requests
import sys
import os
from openai import AzureOpenAI
import tiktoken
from dotenv import load_dotenv
load_dotenv()

# Create an instance of the AzureOpenAI class
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-15-preview"
)

# Select the GPT-4o model for text
model = "gpt-4o-mini"

prompt = "Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches.\n\nTl;dr"

#Setting a few additional, typical parameters during API Call
response = client.chat.completions.create(
  model=model,
  messages = [{"role":"system", "content":"You are a helpful assistant."},
               {"role":"user","content":prompt},])

response.choices[0].message.content

# Imprimir la respuesta generada por el modelo
print("Model response:", response.choices[0].message.content)