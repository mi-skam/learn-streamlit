# Import prerequisite libraries
import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI


load_dotenv()
client = AsyncOpenAI()


async def dall_e(prompt):
    image = await client.images.generate(
            prompt=prompt,
            n=2,
            size="1024x1024"
    )

    return image


async def main():
    # Define the user prompt message
    prompt = "A cute baby sea otter"
    answer = await dall_e(prompt)
    print(answer)


asyncio.run(main())
