# streamlit, a low-code framework used for the front end to let users interact with the app.
# langchain, a framework for working with LLM models.
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# browser window title
st.set_page_config(page_title="Zaitz: blog outline generator")
# app title
st.title("Zaitz: blog outline generator 🎨🤖")


# gets a user's input, sends it to the llm and prints the response in a info box
def generate_response(input_text):
    print(openai_api_key)
    llm = OpenAI(
        model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=openai_api_key
    )
    topic = input_text
    template = "As an experienced data scientist and technical writer, generate an outline for a blog about {topic}."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM Model
    response = llm(prompt_query)

    return st.info(response)


# this context creates a form
with st.form("my_form"):
    topic = st.text_input("Enter keyword:", "")
    # creates a handler for the submit button, returns True if the button was clicked
    submitted = st.form_submit_button("Submit")

    # check for wrong key format
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    # runs generate_response with the input as arguments
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(topic)
