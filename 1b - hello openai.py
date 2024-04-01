# Import prerequisite libraries
import asyncio
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()


def chatgpt_answers(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        stream=True
    )

    for chunk in completion:
        print(chunk.choices[0].delta.content, end='')


def main():
    # Define the user prompt message
    prompt = "Create a blog outline for a post about first day at school"
    chatgpt_answers(prompt)
    


main()