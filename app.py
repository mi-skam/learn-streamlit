# streamlit, a low-code framework used for the front end to let users interact with the app.
# langchain, a framework for working with LLM models.
import streamlit as st
from langchain import PromptTemplate
from langchain_community.llms import OpenAI

# browser window title
st.set_page_config(page_title="Zaitz: blog outline generator")
# app title
st.title("Zaitz: blog outline generator 🎨🤖")

# gets the user's input in a side panel and saves it in openai_api_key
openai_api_key = st.sidebar.text_input("OpenAI API Key")


# gets a user's input, sends it to the llm and prints the response in a info box
def generate_response(input_text):
    llm = OpenAI(
        model_name="text-davinci-003", temperature=0.7, openai_api_key=openai_api_key
    )
    topic = input_text
    template = "As an experienced data scientist and technical writer, generate an outline for a blog about {topic}."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM Model
    response = llm(prompt_query)

    return st.info(generate_response)


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
