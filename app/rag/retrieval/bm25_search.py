from rank_bm25 import BM25Okapi

from app.rag.vectorstore.chroma_client import collection


def bm25_search(question, policy_type=None, top_k=10):

    # Get documents from Chroma
    if policy_type:
        results = collection.get(
            where={
                "policy_type": policy_type
            }
        )
        print("========== BM25 ==========")
        print("Policy Type:", policy_type)
        print("Documents:", len(results["documents"]))
        print("Metadata:", len(results["metadatas"]))
    else:
        results = collection.get()

    documents = results["documents"]
    metadatas = results["metadatas"]

    # Tokenize
    tokenized_docs = [
        doc.lower().split()
        for doc in documents
    ]

    bm25 = BM25Okapi(tokenized_docs)

    tokenized_query = question.lower().split()

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked = sorted(

        zip(scores, documents, metadatas),

        key=lambda x: x[0],

        reverse=True

    )[:top_k]

    for score, doc, metadata in ranked:
        print(
            f"Score={score:.4f} | Chunk={metadata['chunk_index']}"
        )

    final_results = []

    for score, doc, metadata in ranked:

        final_results.append({

            "chunk": doc,

            "metadata": metadata,

            "bm25_score": score
        })

    return final_results