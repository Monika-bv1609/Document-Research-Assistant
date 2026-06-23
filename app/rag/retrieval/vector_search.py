from app.rag.retrieval.embedding_generator import (
    generate_embeddings
)

from app.rag.vectorstore.vector_store import (
    VectorStore
)
from langsmith import traceable

@traceable(name="semantic_search")
def semantic_search(question):

    # Generate embedding
    question_embedding = generate_embeddings(
        [question]
    )[0]

    # Search more chunks
    results = VectorStore.search(

        query_embedding=question_embedding,

        top_k=6
    )

    documents = results["documents"][0]

    metadatas = results["metadatas"][0]

    final_results = []

    seen_sources = set()

    for doc, metadata in zip(

        documents,

        metadatas
    ):

        source = metadata["source"]

        # Avoid duplicate chunks from same PDF
        if source in seen_sources:

            continue

        seen_sources.add(source)

        final_results.append({

            "chunk": doc,

            "metadata": metadata
        })

    return final_results