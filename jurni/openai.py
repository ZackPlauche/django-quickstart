from dataclasses import dataclass
import os
import openai

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

GPT_MODEL = 'gpt-3.5-turbo'


def get_response(messages: list[dict]):
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=messages
    )
    return response


def get_message(messages: list[dict]):
    response = get_response(messages)
    return response['choices'][0]['message']