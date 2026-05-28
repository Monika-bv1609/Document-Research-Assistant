import requests
import os

from dotenv import load_dotenv

load_dotenv()


def generate_embeddings(chunks: list):

    url = "https://api.jina.ai/v1/embeddings"

    headers = {

        "Content-Type":
        "application/json",

        "Authorization":
        f"Bearer {os.getenv('JINA_API_KEY')}"
    }

    data = {

        "model":
        "jina-embeddings-v2-base-en",

        "input":
        chunks
    }

    response = requests.post(

        url,

        headers=headers,

        json=data
    )

    if response.status_code != 200:

        raise Exception(
            f"Embedding API Error: {response.text}"
        )

    result = response.json()

    embeddings = [

        item["embedding"]

        for item in result["data"]
    ]

    return embeddings