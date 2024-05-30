import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI bot. You will help the user in his queries"),
        ("user", "Question : {question}")
    ]
)

st.title('Langchain Demo with Ollama models')
input_text = st.text_input("Ask any question : ")

llm_model = Ollama(model = 'llama2')
output_parser = StrOutputParser()

chain = prompt|llm_model|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
