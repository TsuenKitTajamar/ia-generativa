import re
import requests
import sys
import os
from openai import AzureOpenAI
import tiktoken
import numpy as np
from dotenv import load_dotenv
load_dotenv()

# Create an instance of the AzureOpenAI class
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-15-preview"
)

model="text-embedding-ada-002"

def cosine_similarity(query_embedding, embeddings, distance_metric='cosine'):
    if distance_metric == 'cosine':
        distances = np.dot(embeddings, query_embedding) / (np.linalg.norm(embeddings) * np.linalg.norm(query_embedding))
        distances = 1 - distances  
    else:
        raise ValueError("Métrica de distância não suportada. Utilize 'cosine'.")

    return distances

text = 'the quick brown fox jumped over the lazy dog'
client.embeddings.create(input=[text], model="text-embedding-ada-002").data[0].embedding
print(text)

# compare several words
automobile_embedding    = client.embeddings.create(input='automobile', model=model).data[0].embedding
vehicle_embedding       = client.embeddings.create(input='vehicle', model=model).data[0].embedding
dinosaur_embedding      = client.embeddings.create(input='dinosaur', model=model).data[0].embedding
stick_embedding         = client.embeddings.create(input='stick', model=model).data[0].embedding

print(cosine_similarity(automobile_embedding, vehicle_embedding))
print(cosine_similarity(automobile_embedding, dinosaur_embedding))
print(cosine_similarity(automobile_embedding, stick_embedding))

# El objetivo de este código es calcular la similitud de coseno entre las representaciones de palabras (embeddings) generadas por un modelo de lenguaje (en este caso, el modelo text-embedding-ada-002 de OpenAI).
# Los valores de similitud de coseno que ves son pequeños, lo que indica que, en el espacio de embeddings de este modelo, estas palabras no son demasiado cercanas entre sí. Esto puede deberse a cómo el modelo ha aprendido las relaciones semánticas entre ellas.
