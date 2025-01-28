# IAG Module - Modulo de IAG - Inteligencia Artificial Generativa
## Configuration
1.Install necessary libraries:
- Install `OpenAI` library in your python environment
```python
pip install openai
```
- Load standard helper libraries and set your typical OpenAI security credentials for the OpenAI Service that you've created
```python
pip install python-dotenv
```
- Create a `.env` file to save your Azure credentials where the following code will access to the `KEY` and `ENDPOINT`
```python
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
```

Your `.env` will be like the following sample:
```python
AZURE_OPENAI_ENDPOINT = "YOUR_AZURE_ENDPOINT" 
AZURE_OPENAI_API_KEY = "YOUR_AZURE_OPENAI_API_KEY"
```

## Exercises List
1. Exercise 01 - Practica Preprocesamiento de texto para OpenAI -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/tree/main/preprocessing)
2. Exercise 02 - OpenAI Getting Started 1 -> [Enlace a la guía de Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Ckeyless%2Cjavascript-keyless%2Ctypescript-keyless%2Cpython-new&pivots=programming-language-python)
3. Exercise 03 - OpenAI Getting Started 2 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/01_OpenAI_getting_started.ipynb)
4. Exercise 04 - Desarrollando barreras contra las alucinaciones -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/Developing_hallucination_guardrails.ipynb)
5. Exercise 05 - Utilización del SDK de OpenAI para python -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/quickstart.ipynb)
6. Exercise 06 - WebApp: Resumen de Emails -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/email_app.md)
7. Exercise 07 - Práctica Filtrado de contenido en OpenAI -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/chat.ipynb)
8. Exercise 08 - Java Aplicacion con SpringBoot integrado con OpenAI -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/tree/main/Spring%20AI%20with%20Azure%20OpenAI%20Service)
    - [Demos Video Link](https://tajamar365-my.sharepoint.com/:f:/p/tsuenkit_lui/EiQUEAP_SxpDrmTd3cMPkjEBKVfm-jdNKsqmU6PO7tSWGQ?e=h54QYu)
9. Exercise 09 
    - Practica Embeddings 1 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/basic_embeddings_example_restapi.ipynb)
    - Practica Embeddings 2 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/embeddings.ipynb)
    - Practica Embeddings 3 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/Embedding_long_inputs.ipynb)
10. Exercise 10
    - Restringir acceso a OpenAI a una subred
11. Exercise 11
    - Ejercicios de Ingenieria del Prompt 1 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/tree/main/Prompt-Engineering-Exercises)
    - Ejercicios de Ingenieria del Prompt 2 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/05_OpenAI_parameters.ipynb)
    - Ejercicios de Ingenieria del Prompt 3 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/06_best_practice-prompt-engineering.ipynb)
    - Ejercicios de Ingenieria del Prompt 4 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/07_prompt_engineering.ipynb)
12. Exercise 12
    - Fine Tuning Data preparation -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/tree/main/fine-tuned_qa-rag)
13. Exercise 13
    - Generative search (RAG) with grounding data from Azure AI Search -> [Microsoft Learn guide](https://learn.microsoft.com/en-us/azure/search/search-get-started-rag)
14. Exercise 14
    - Fine Tuning con OpenAI (tuning gpt-4o-mini) -> [Microsoft Learn guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line)
15. Exercise 15
    - Gestión de conversacion con OpenAI -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/chatGPT_managing_conversation.ipynb)
16. Exercise 16
    - Generate images with a DALL-E model -> [Microsoft Learn guide](https://microsoftlearning.github.io/mslearn-openai/Instructions/Exercises/05-generate-images.html)

