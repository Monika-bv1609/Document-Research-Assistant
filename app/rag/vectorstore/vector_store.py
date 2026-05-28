from app.rag.vectorstore.chroma_client import collection


class VectorStore:

    @staticmethod
    def add_documents(

        chunks,

        embeddings,

        metadata_list,

        ids
    ):

        collection.add(

            documents=chunks,

            embeddings=embeddings,

            metadatas=metadata_list,

            ids=ids
        )

    @staticmethod
    def search(

        query_embedding,

        top_k=5
    ):

        results = collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k
        )

        return results

    @staticmethod
    def document_exists(filename):

        results = collection.get()

        metadatas = results.get(
            "metadatas",
            []
        )

        for metadata in metadatas:

            if metadata["source"] == filename:

                return True

        return False