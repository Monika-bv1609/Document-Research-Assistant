from sklearn.metrics.pairwise import (
    cosine_similarity
)

import requests

import os

from dotenv import (
    load_dotenv
)

load_dotenv()


def generate_query_embedding(
    query: str
):

    url = (
        "https://api.jina.ai/v1/embeddings"
    )

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
        [query]
    }

    response = requests.post(

        url,

        headers=headers,

        json=data
    )

    result = response.json()

    embedding = (
        result["data"][0]["embedding"]
    )

    return [embedding]


def semantic_search(

    query: str,

    chunks: list,

    chunk_embeddings,

    top_k: int = 3
):

    query_embedding = (
        generate_query_embedding(
            query
        )
    )

    similarities = cosine_similarity(

        query_embedding,

        chunk_embeddings
    )[0]

    top_indices = similarities.argsort()[

        -top_k:

    ][::-1]

    relevant_chunks = []

    for index in top_indices:

        print(
            "MATCH SCORE:",
            similarities[index]
        )

        relevant_chunks.append(
            chunks[index]
        )

    return relevant_chunks