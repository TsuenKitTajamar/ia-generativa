import os
from openai import AzureOpenAI
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

# Descripción de la startup
description = "Estamos buscando ideas para una startup en el campo de inteligencia artificial, enfocada en la salud."

# Crear el prompt para generar ideas
prompt = f"Genera 10 ideas de negocios para una startup tecnológica en el área de inteligencia artificial. La idea debe estar enfocada en: {description}"
print(prompt)

# Llamada a la API de OpenAI
response = client.chat.completions.create(
       model=model,
  messages = [{"role":"system", "content":"You are a helpful assistant."},
               {"role":"user","content":prompt},]
)

response.choices[0].message.content

# Imprimir la respuesta generada por el modelo
print("Model response:", response.choices[0].message.content)