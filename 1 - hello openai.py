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
    )

    return completion.choices[0].message.content


def main():
    # Define the user prompt message
    prompt = "Hello"
    answer = chatgpt_answers(prompt)
    print(answer)


main()
