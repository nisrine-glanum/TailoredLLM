"""
Created on Tue Apr 25 12:43:13 2023

@author: Nisrine
"""
#Imports
import streamlit as st
import requests
import os
from paradigm_client.remote_model import RemoteModel
from langchain.prompts import PromptTemplate
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
    ("Summarization", "LightOn LLM", "Backlog")
)

other_selectbox = st.sidebar.selectbox(
    "Custom pipeline :",
    ("Conversational", "Text generation", "Text2Text generation", "Question answering"), disabled = True
)

if add_selectbox == "Backlog":
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

os.environ["PARADIGM_API_KEY"] = "yqa3tBQp.YNXQ5aWtr5j1ZX97cGLV9gFgbphNFOnE"
os.environ["HOST"] = "https://llm.lighton.ai"
host = os.environ.get('HOST')
model = RemoteModel(host, model_name="llm-mini")

lighton_model = {
    '' : '',
    'LightOn' : model,
}

if add_selectbox == "LightOn LLM":
    st.warning("Testing LightOn LLM")
    txt = st.text_area('Put the text to FALC here')

    option = st.selectbox(
        'Choose a model',
        (list(lighton_model.keys()))
    )

    if st.button('Click here to FALC the text'):
        if option == "Open-assistant":
            output = query(
                {"inputs": "<|prompter|> " + txt + ". Peux-tu faire un résumé d'un texte ?<|endoftext|><|assistant|>"},
                str(lighton_model[option]))
            try:
                st.write("The simplified version of your text is :")
                st.success(output[0]["summary_text"])
                text_contents = output[0]["summary_text"]
                st.download_button('Download', text_contents)
            except KeyError:
                st.error(output["error"] + ". \n\n Wait a moment for the model to load and retry later !", icon="🚨")
        elif (option != '') and (option in lighton_model):
            output = query({"inputs": txt}, str(lighton_model[option]))
            try:
                st.write("The simplified version of your text is :")
                st.success(output[0]["summary_text"])
                text_contents = output[0]["summary_text"]
                st.download_button('Download', text_contents)
            except KeyError:
                st.error(output["error"] + ". \n\n Wait a moment for the model to load and retry later !", icon="🚨")

summarization_models = {
    '' : '',
    'Barthez-orangesum-abstract' : 'https://api-inference.huggingface.co/models/moussaKam/barthez-orangesum-abstract',
    'MT5_multilingual_XLSum' : 'https://api-inference.huggingface.co/models/csebuetnlp/mT5_multilingual_XLSum',
    'Camembert' : "https://api-inference.huggingface.co/models/mrm8488/camembert2camembert_shared-finetuned-french-summarization",
    'MT5_m2m_crossSum' : "https://api-inference.huggingface.co/models/csebuetnlp/mT5_m2m_crossSum",
    'T5-base-fr-sum-cnndm' : "https://api-inference.huggingface.co/models/plguillou/t5-base-fr-sum-cnndm",
    'Open-assistant' : "https://api-inference.huggingface.co/models/OpenAssistant/stablelm-7b-sft-v7-epoch-3"
}
    
if add_selectbox == "Summarization":
    st.warning("Please be warned that some models take a while to load and some of them give inaccurate results.")
    txt = st.text_area('Put the text to FALC here')
    
    option = st.selectbox(
        'Choose a model',
        (list(summarization_models.keys()))
    )

    if st.button('Click here to FALC the text'):
        if option == "Open-assistant":
            output = query({"inputs": "<|prompter|> " + txt + ". Peux-tu faire un résumé d'un texte ?<|endoftext|><|assistant|>"}, str(summarization_models[option]))
            try:
                st.write("The simplified version of your text is :")
                st.success(output[0]["summary_text"])
                text_contents = output[0]["summary_text"]
                st.download_button('Download', text_contents)
            except KeyError:
                st.error(output["error"] + ". \n\n Wait a moment for the model to load and retry later !", icon="🚨")
        elif (option != '') and (option in summarization_models):
            output = query({"inputs": txt}, str(summarization_models[option]))
            try:
                st.write("The simplified version of your text is :")
                st.success(output[0]["summary_text"])
                text_contents = output[0]["summary_text"]
                st.download_button('Download', text_contents)
            except KeyError:
                st.error(output["error"] + ". \n\n Wait a moment for the model to load and retry later !", icon="🚨")


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
            text_contents = output[0]["generated_text"]
            st.download_button('Download', text_contents)
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
