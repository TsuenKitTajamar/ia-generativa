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
1. Exercise 1 - Practica Preprocesamiento de texto para OpenAI -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/tree/main/preprocessing)
2. Exercise 2 - OpenAI Getting Started 1 -> [Enlace a la guía](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Ckeyless%2Cjavascript-keyless%2Ctypescript-keyless%2Cpython-new&pivots=programming-language-python)
3. Exercise 3 - OpenAI Getting Started 2 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/01_OpenAI_getting_started.ipynb)
4. Exercise 4 - Desarrollando barreras contra las alucinaciones -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/Developing_hallucination_guardrails.ipynb)
5. Exercise 5 - Utilización del SDK de OpenAI para python -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/quickstart.ipynb)
6. Exercise 6 - WebApp: Resumen de Emails -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/email_app.md)
7. Exercise 7 - Práctica Filtrado de contenido en OpenAI -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/chat.ipynb)
8. Exercise 8 - Java Aplicacion con SpingBoot integrado con OpenAI -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/tree/main/Spring%20AI%20with%20Azure%20OpenAI%20Service)
    - [Demos Video Link](https://tajamar365-my.sharepoint.com/:f:/p/tsuenkit_lui/EiQUEAP_SxpDrmTd3cMPkjEBKVfm-jdNKsqmU6PO7tSWGQ?e=h54QYu)
9. Exercise 9 - Practica Embeddings 1 -> [Enlace al repositorio](https://github.com/tamasma/master-ia-tajamar/blob/main/basic_embeddings_example_restapi.ipynb)