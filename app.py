import streamlit as st
import os
from paradigm_client.remote_model import RemoteModel

st.title('Tailored LLMs _by Glanum_')
st.header('Use case : Unapei')
st.divider()

os.environ["PARADIGM_API_KEY"] = "yqa3tBQp.YNXQ5aWtr5j1ZX97cGLV9gFgbphNFOnE"
os.environ["HOST"] = "https://llm.lighton.ai"

host = os.environ.get('HOST')

model = RemoteModel(host, model_name="llm-mini")

print(model.create("bonjour, ").completions[0].output_text)
