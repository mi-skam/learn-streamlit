import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image

# load OpenAI key
load_dotenv()
openai = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.set_page_config(page_title="ChatGPT + DALL-E 2")


@st.cache(
    persist=True,
    allow_output_mutation=True,
    show_spinner=False,
    suppress_st_warning=True,
)
def openai_completion(prompt):
    completion = openai.completions.create(
        model="text-davinci-003", prompt=prompt, max_tokens=150, temperature=0.5
    )
    return completion.choices[0].text


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


format_type = st.sidebar.selectbox("Choose your AI", ["ChatGPT", "DALL-E 2"])

if format_type == "ChatGPT":
    input_text = st.text_area("Prompt", height=50)
    chat_button = st.button("Send")

    if chat_button and input_text.strip() != "":
        with st.spinner("Loading..."):
            openai_answer = openai_completion(input_text)
            st.success(openai_answer)
    else:
        st.warning("Please enter something.")
