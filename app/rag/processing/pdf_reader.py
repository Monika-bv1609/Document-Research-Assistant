from pypdf import PdfReader

from app.rag.processing.text_chunker import (
    chunk_text
)

from app.rag.retrieval.embedding_generator import (
    generate_embeddings
)

from app.rag.vectorstore.vector_store import (
    VectorStore
)


def read_pdf(

    file_path: str,

    filename: str,
    
    policy_type: str
):

    try:

        # Check duplicate PDF
        if VectorStore.document_exists(filename):

            print("Document already exists.")

            return []

        # Open PDF
        reader = PdfReader(file_path)

        text = ""

        # Read all pages
        for page in reader.pages:

            page_text = page.extract_text()

            # Normalize spaces
            page_text = " ".join(
                page_text.split()
            )

            text += page_text + "\n"

        # Create chunks
        chunks = chunk_text(text)

        print(f"00000000000 TOTAL CHUNKS CREATED = {len(chunks)}")

        # Generate embeddings
        embeddings = generate_embeddings(
            chunks
        )

        # Create metadata
        metadata_list = []

        for index, chunk in enumerate(chunks):

            metadata_list.append({

                "source": filename,

                "chunk_index": index,

                "policy_type": policy_type
            })

        # Create unique IDs
        ids = [

            f"{filename}_{i}"

            for i in range(len(chunks))
        ]


        # Store in ChromaDB
        VectorStore.add_documents(

            chunks=chunks,

            embeddings=embeddings,

            metadata_list=metadata_list,

            ids=ids
        )

        results = collection.get(
            where={"policy_type": policy_type}
        )

        print("TOTAL STORED:", len(results["ids"]))

        for metadata in results["metadatas"][:5]:
            print(metadata)

        return chunks

    except Exception as e:

        print(e)

        return "PDF reading failed."