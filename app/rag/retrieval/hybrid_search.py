from app.rag.retrieval.vector_search import semantic_search
from app.rag.retrieval.bm25_search import bm25_search


def hybrid_search(question, policy_type=None):

    print("\n========== HYBRID SEARCH ==========")

    # Semantic Search
    vector_results = semantic_search(
        question,
        policy_type=policy_type
    )

    # BM25 Search
    bm25_results = bm25_search(
        question,
        policy_type=policy_type
    )

    print(f"Vector Results : {len(vector_results)}")
    print(f"BM25 Results   : {len(bm25_results)}")

    merged = vector_results + bm25_results

    unique_chunks = {}

    for result in merged:

        key = (
            result["metadata"]["source"],
            result["metadata"]["chunk_index"]
        )

        if key not in unique_chunks:
            unique_chunks[key] = result

    final_results = list(
        unique_chunks.values()
    )

    print(
        f"Hybrid Results : {len(final_results)}"
    )

    print("===============================\n")

    return final_results