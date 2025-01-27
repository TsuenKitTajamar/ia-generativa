import os
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv

# Loading environment variables from the .env file
load_dotenv()

# Create an AzureOpenAI instance
client = AzureOpenAI( 
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), #  - azure_endpoint: URL de la instancia de Azure OpenAI
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  #  - api_key: Clave de la instancia de Azure OpenAI
  api_version="2024-02-01" #  - api_version: Versión de la API de Azure OpenAI
)

model="gpt-4o-mini"

#Streamlit UI
def app():
    # App title
    st.title("Email Assistant App")

    # Instructions for the app
    st.write("This is a simple email assistant app :sunglasses: .")
    st.write("Enter an email and click one of the buttons below to get a :blue[summary] or an :red[answer].")

    # Text area to enter the email
    email_content = st.text_area("Enter your email content here:")
    print(email_content)

    # Button to generate summary
    if st.button("Generate Summary"): # if the button is clicked = true
        if email_content: # if the email_content is NOT empty
            st.write("Generating summary...")
            summary = generate_summary(email_content.strip()) # Generate summary using Azure OpenAI | strip() removes leading and trailing whitespaces
            st.write("Summary:", summary)
        else:
            st.write("Please enter an email to summarize.") # if the email_content is empty

    # Button to generate answer
    if st.button("Generate Answer"): # if the button is clicked = true
        if email_content: # if the email_content is NOT empty
            st.write("Generating answer...") 
            answer = generate_answer(email_content.strip()) # Generate answer using Azure OpenAI | strip() removes leading and trailing whitespaces
            st.write("Answer:", answer)
        else:
            st.write("Please enter an email to generate an answer.") # if the email_content is empty

# Function to generate summary using Azure OpenAI
def generate_summary(email_content):
    response = client.chat.completions.create( # Create a conversation
        model=model, 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize this email: {email_content}"} # Summarize the email
        ]
    )
    return response.choices[0].message.content

# Function to generate an answer using Azure OpenAI
def generate_answer(email_content):
    response = client.chat.completions.create( # Create a conversation
        model=model, 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."}, 
            {"role": "user", "content": f"Provide an answer to this email: {email_content}"} # Provide an answer to the email
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    app() # Run the Streamlit app