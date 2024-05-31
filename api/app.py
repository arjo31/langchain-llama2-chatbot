from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="Langchain Server using FastAPI",
    version="1.0",
    description="A simple API Server"
)

model1 = Ollama(model="llama2")
model2 = Ollama(model="moondream")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} in about 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} in about 50 words")

add_routes(
    app,
    prompt1|model1,
    path="/essay"
)

add_routes(
    app,
    prompt2|model2,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)
