"""
Created on Tue Apr 25 12:43:13 2023

@author: Nisrine
"""
#Imports
import streamlit as st
import requests
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.environ.get("API_KEY")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload, model):
    response = requests.post(model, headers=headers, json=payload)
    return response.json()

st.title('Tailored LLMs _by Glanum_')
st.header('Use case : Unapei')
st.divider()

add_selectbox = st.sidebar.selectbox(
    "NLP tasks :",
    ("Home", "Summarization", "Conversational", "Text generation", "Text2Text generation", "Question answering")
)

if add_selectbox == "Home":
    st.header("Backlog of ideas to implement : ")
    st.divider()
    
    st.info('Feature 1 : Upload the original text')
    
    uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
    
    st.divider()
    
    st.info("Feature 2 : Download the generated text")
    
    text_contents = '''This is some FALC text'''
    st.download_button('Download', text_contents)
    
    st.divider()

summarization_models = {
    '' : '',
    'barthez-orangesum-abstract' : 'https://api-inference.huggingface.co/models/moussaKam/barthez-orangesum-abstract',
    'mT5_multilingual_XLSum' : 'https://api-inference.huggingface.co/models/csebuetnlp/mT5_multilingual_XLSum',
    'camembert' : "https://api-inference.huggingface.co/models/mrm8488/camembert2camembert_shared-finetuned-french-summarization",
    'mT5_m2m_crossSum' : "https://api-inference.huggingface.co/models/csebuetnlp/mT5_m2m_crossSum",
    't5-base-fr-sum-cnndm' : "https://api-inference.huggingface.co/models/plguillou/t5-base-fr-sum-cnndm"
}
    
if add_selectbox == "Summarization":
    txt = st.text_area('Text to FALC')
    
    option = st.selectbox(
        'Choose a model to FALC your text?',
        (list(summarization_models.keys()))
    )

    st.write('Result :')
    
    if (option != '') and (option in summarization_models):
        output = query({ "inputs": txt}, str(summarization_models[option]))
        try:
            st.write(output[0]["summary_text"]) 
        except KeyError:
            st.write(output["error"])
            st.write("Retry later !")


conversational_models = {
    '' : '',
    'mGPT' : "https://api-inference.huggingface.co/models/ai-forever/mGPT"
}

if add_selectbox == "Conversational":
    txt = st.text_area('Text to FALC')
    
    option = st.selectbox(
        'Choose a model to FALC your text?',
        (list(conversational_models.keys()))
    )

    st.write('Result :')
    
    if (option != '') and (option in conversational_models):
        output = query({ "inputs": txt}, str(conversational_models[option]))
        try:
            st.write(output[0]["generated_text"]) 
        except KeyError:
            st.write(output["error"])
            st.write("Retry later !")
        
        
generation_models = {
    '' : '',
    'GPT2' : "https://api-inference.huggingface.co/models/ClassCat/gpt2-base-french"
}

if add_selectbox == "Text generation":
    txt = st.text_area('Text to FALC')
    
    option = st.selectbox(
        'Choose a model to FALC your text?',
        (list(generation_models.keys()))
    )

    st.write('Result :')
    
    if (option != '') and (option in generation_models):
        output = query({ "inputs": txt}, str(generation_models[option]))
        try:
            st.write(output[0]["generated_text"]) 
        except KeyError:
            st.write(output["error"])
            st.write("Retry later !")
