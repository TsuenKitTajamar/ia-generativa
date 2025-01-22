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

# Contextos de preguntas
questions = [
    {"context": "Responde como un asistente virtual médico.", "question": "¿Cuáles son los síntomas comunes de la gripe?"},
    {"context": "Responde como un asistente virtual para clientes.", "question": "¿Cuál es la política de devoluciones de productos?"}
]

# Llamada a la API para cada pregunta
for q in questions:
    prompt = f"Contexto: {q['context']}\nPregunta: {q['question']}\nRespuesta:"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    # Imprimir pregunta y respuesta del modelo
    print(f"Pregunta:\n {q['question']}")
    print(f"Respuesta del modelo:\n {response.choices[0].message.content}\n")
