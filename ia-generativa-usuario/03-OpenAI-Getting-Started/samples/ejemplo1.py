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

response = client.chat.completions.create( # Call the chat endpoint
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, # System message behavior
        {"role": "user", "content": "Knock knock."}, # User message 
        {"role": "assistant", "content": "Who's there?"}, # Assistant message
        {"role": "user", "content": "Orange."},
    ],
    temperature=0,
)

print(f"{response.choices[0].message.role}: {response.choices[0].message.content}")
