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

prompt = "Classify the following inquiry into one of the following: categories: [Pricing, Hardware Support, Software Support]\n\ninquiry: Hello, one of the keys on my laptop keyboard broke recently and I'll need a replacement:\n\nClassified category:"
print(prompt)

#Setting a few additional, typical parameters during API Call
response = client.chat.completions.create(
       model=model,
  messages = [{"role":"system", "content":"You are a helpful assistant."},
               {"role":"user","content":prompt},])

response.choices[0].message.content

# Imprimir la respuesta generada por el modelo
print("Model response:", response.choices[0].message.content)