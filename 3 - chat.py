# Import prerequisite libraries
import asyncio
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()


def chatgpt_answers(messages):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
    )

    return completion.choices[0].message.content

def display_chat_history(messages):
    for message in messages:
        print(f"{message['role'].capitalize()}: {message['content']}")


def main():
    # Define the user prompt message
    prompt = "Hello"
    messages = [{"role": "assistant", "content": "How can I help?"}]
    
    while True:
        display_chat_history(messages)
        
        prompt = input("User: ")
        messages.append({"role": "user", "content": prompt})
        
        answer = chatgpt_answers(messages)
        messages.append({"role": "assistant", "content": answer})

main()
