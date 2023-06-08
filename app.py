import streamlit as st
import os
from paradigm_client.remote_model import RemoteModel

st.title('Tailored LLMs _by Glanum_')
st.header('Use case : Unapei')
st.divider()

add_selectbox = st.sidebar.selectbox(
    "Pipeline :",
    ("LightOn LLM")
)

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
