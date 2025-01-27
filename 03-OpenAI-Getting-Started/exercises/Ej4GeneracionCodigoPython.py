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

# Problema matemático
problem = "Escribe un programa en Python que calcule el área de un triángulo dado su base y su altura."

# Crear el prompt para generar código
prompt = f"Escribe un código en Python para resolver el siguiente problema: {problem}"
print(prompt)

# Llamada a la API de OpenAI
response = client.chat.completions.create(
       model=model,
  messages = [{"role":"system", "content":"Eres un experto en programación Python."},
               {"role":"user","content":prompt},]
)

response.choices[0].message.content

# Imprimir la respuesta generada por el modelo
print("Model response:", response.choices[0].message.content)

# Ejemplo de uso
base = 5
altura = 10
##area = calcular_area_triangulo(base, altura)
##print(f"El área del triángulo es: {area}")