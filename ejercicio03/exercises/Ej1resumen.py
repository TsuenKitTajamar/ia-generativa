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

# Ingresar un artículo largo
text = """
El cambio climático es uno de los mayores desafíos a los que se enfrenta la humanidad en el siglo XXI. 
Los científicos han demostrado que la actividad humana, como la quema de combustibles fósiles, es responsable de un aumento sin precedentes en las temperaturas globales. 
Este fenómeno tiene consecuencias devastadoras para los ecosistemas, la biodiversidad, y la salud humana. Se prevé que si no se toman medidas drásticas, los efectos del cambio climático serán irreversibles.
"""

# Crear el prompt para obtener un resumen estructurado
prompt = f"Genera un resumen estructurado en formato de esquema con títulos y subtítulos del siguiente artículo:\n\n{text}"
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