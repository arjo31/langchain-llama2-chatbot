import requests
import streamlit as st

def get_llama2_response(input_text):
    try:
        response = requests.post("http://localhost:8000/essay/invoke", json={'input': {'topic': input_text}})
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        # print(data)  # Log the full response for debugging
        return data['output']
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return "An error occurred while processing your request."
    except KeyError:
        print("Unexpected response structure:", data)
        return "Received unexpected response from the server."

def get_moondream_response(input_text):
    try:
        response = requests.post("http://localhost:8000/poem/invoke", json={'input': {'topic': input_text}})
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        # print(data)  # Log the full response for debugging
        return data['output']
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return "An error occurred while processing your request."
    except KeyError:
        print("Unexpected response structure:", data)
        return "Received unexpected response from the server."

st.title('Langchain Chatbot With API Chains')
essay_text = st.text_input('Write an essay on : ')
poem_text = st.text_input('Write a poem on : ')

if essay_text:
    text = get_llama2_response(essay_text)
    st.write(text)

if poem_text:
    text = get_moondream_response(poem_text)
    st.write(text)