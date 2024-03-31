# streamlit, a low-code framework used for the front end to let users interact with the app.
# langchain, a framework for working with LLM models.
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# load OpenAI key
load_dotenv()
try:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
except Exception:
    # gets the user's input in a side panel and saves it in openai_api_key
    openai_api_key = st.sidebar.text_input("OpenAI API Key")
    client = OpenAI(api_key=openai_api_key)


@st.cache_data(
    persist=True,
    show_spinner=False,
)
def openai_completion(prompt):
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=150, temperature=0.5
    )
    return completion.choices[0].text


@st.cache_data(
    persist=True,
    show_spinner=False,
)
def openai_image(prompt):
    image = client.images.generate(prompt=prompt, n=1, size="512x512")
    image_url = image.data[0].url
    return image_url


format_type = st.sidebar.selectbox("Choose your AI", ["ChatGPT", "DALL-E 2"])

if format_type == "ChatGPT":
    input_text = st.text_area("Prompt", height=50)
    chat_button = st.button("Chat")

    if chat_button and input_text.strip() != "":
        with st.spinner("Loading..."):
            openai_answer = openai_completion(input_text)
            st.success(openai_answer)
    else:
        st.warning("Please enter something.")

elif format_type == "DALL-E 2":
    input_text = st.text_area("Prompt", height=50)
    image_button = st.button("Generate Image")

    if image_button and input_text.strip() != "":
        with st.spinner("Loading..."):
            image_url = openai_image(input_text)
            st.image(image_url)
    else:
        st.warning("Please enter something")
