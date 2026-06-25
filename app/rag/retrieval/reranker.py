import requests
import os

from dotenv import load_dotenv
from langsmith import traceable

load_dotenv()


@traceable(name="jina_rerank")
def rerank_chunks(question, chunks, top_n=3):

    if not chunks:
        return []

    url = "https://api.jina.ai/v1/rerank"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('JINA_API_KEY')}"
    }

    data = {
        "model": "jina-reranker-v2-base-multilingual",
        "query": question,
        "documents": [
            chunk["chunk"]
            for chunk in chunks
        ],
        "top_n": top_n
    }

    print("Chunks received by reranker:", len(chunks))

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    if response.status_code != 200:
        raise Exception(
            f"Reranker Error: {response.text}"
        )

    results = response.json()["results"]

    print("Results returned by Jina:", len(results))

    reranked_chunks = []

    print("\n========== RERANKING ==========")

    for result in results:

        index = result["index"]

        score = result["relevance_score"]

        print(
            f"Score={score:.4f} | "
            f"Source={chunks[index]['metadata']['source']} | "
            f"Chunk={chunks[index]['metadata']['chunk_index']}"
        )

        reranked_chunks.append(
            chunks[index]
        )

    print("===============================\n")

    print("Chunks after reranking:", len(reranked_chunks))

    return reranked_chunks