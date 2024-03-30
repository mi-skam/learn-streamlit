# streamlit, a low-code framework used for the front end to let users interact with the app.
# langchain, a framework for working with LLM models.
import streamlit as st
from langchain_community.llms import OpenAI

# app title
st.title("Zaitz 🎨🤖")

# gets the user's input in a side panel and saves it in openai_api_key
openai_api_key = st.sidebar.text_input("OpenAI API Key")


# gets a user's input, sends it to the llm and prints the response in a info box
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


# this context creates a form
with st.form("my_form"):
    # this creates a text area with a placeholder text
    text = st.text_area(
        "Enter text:",
        "How can I create my own LLM frontends, robots and more? I want to use OpenAI, Streamlit and LangChain?",
    )
    # creates a handler for the submit button, returns True if the button was clicked
    submitted = st.form_submit_button("Submit")
    # check for wrong key format
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    # runs generate_response with the input as arguments
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)