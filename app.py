import os
import openai
import streamlit as st
from PIL import Image
from dotenv import load_dotenv

# load OpenAI key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="ChatGPT + DALL-E 2")


@st.cache(
    persist=True,
    allow_output_mutation=True,
    show_spinner=False,
    suppress_st_warning=True,
)
def openai_completion(prompt):
    response = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=150, temperature=0.5
    )
    return response["choices"][0]["text"]


@st.cache(
    persist=True,
    allow_output_mutation=True,
    show_spinner=False,
    suppress_st_warning=True,
)
def openai_image(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size="256x256")
    image_url = response["data"][0]["url"]
    return image_url


format_type = st.sidebar.selectbox(
    "Choose your OpenAI magician 😉", ["ChatGPT", "DALL-E 2"]
)
