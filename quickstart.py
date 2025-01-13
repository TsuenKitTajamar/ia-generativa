import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Crear una instancia de AzureOpenAI
client = AzureOpenAI( 
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), #  - azure_endpoint: URL de la instancia de Azure OpenAI
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  #  - api_key: Clave de la instancia de Azure OpenAI
  api_version="2024-02-01" #  - api_version: Versión de la API de Azure OpenAI
)

# Crear una conversación
response = client.chat.completions.create(
    #gpt-4o-mini or gpt-35-turbo
    model="gpt-4o-mini", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

# Imprimir la respuesta
print(response.choices[0].message.content)