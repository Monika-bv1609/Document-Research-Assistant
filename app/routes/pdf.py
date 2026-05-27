from typing import List

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil

from app.rag.processing.pdf_reader import (
    read_pdf
)

from app.rag.retrieval.embedding_generator import (
    generate_embeddings
)

from app.rag.retrieval.vector_search import (
    semantic_search
)

from app.rag.generation.rag_answer_generator import (
    generate_rag_answer
)

router = APIRouter()

# Store document chunks
DOCUMENT_CHUNKS = []

# Store embeddings
DOCUMENT_EMBEDDINGS = []

# Store metadata
DOCUMENT_METADATA = []

# Chat memory
CHAT_HISTORY = []


@router.post(
    "/read-pdf"
)
async def read_pdf_file(

    files: List[UploadFile] = File(...)
):

    global DOCUMENT_CHUNKS
    global DOCUMENT_EMBEDDINGS
    global DOCUMENT_METADATA

    results = []

    for file in files:

        # Save uploaded PDF
        file_path = (
            f"temp_{file.filename}"
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        # Extract chunks
        chunks = read_pdf(
            file_path
        )

        # Create metadata
        metadata = []

        for chunk in chunks:

            metadata.append({

                "filename":
                file.filename
            })

        # Store chunks
        DOCUMENT_CHUNKS.extend(
            chunks
        )

        # Store metadata
        DOCUMENT_METADATA.extend(
            metadata
        )

        # Generate embeddings
        embeddings = (
            generate_embeddings(
                chunks
            )
        )

        # Store embeddings
        DOCUMENT_EMBEDDINGS.extend(
            embeddings
        )

        results.append({

            "filename":
            file.filename,

            "total_chunks":
            len(chunks),

            "message":
            "PDF processed successfully"
        })

    return {

        "uploaded_files":
        results
    }


@router.post(
    "/ask-pdf"
)
async def ask_pdf(

    question: str
):

    global DOCUMENT_CHUNKS
    global DOCUMENT_EMBEDDINGS
    global DOCUMENT_METADATA
    global CHAT_HISTORY

    # Check if PDF uploaded
    if not DOCUMENT_CHUNKS:

        return {

            "answer":
            "Please upload PDFs first."
        }

    # Retrieve relevant chunks
    relevant_chunks = semantic_search(

        question,

        DOCUMENT_CHUNKS,

        DOCUMENT_EMBEDDINGS,

        DOCUMENT_METADATA
    )

    # Merge top chunk contexts
    context = "\n\n".join(

        [
            result["chunk"]

            for result in relevant_chunks
        ]
    )

    # Source attribution
    source = (
        relevant_chunks[0]["metadata"]["filename"]
    )

    # Build conversation memory
    conversation_context = ""

    for chat in CHAT_HISTORY:

        conversation_context += (

            f"User: {chat['question']}\n"

            f"Assistant: {chat['answer']}\n\n"
        )

    # Combine memory + retrieved context
    full_context = (

        conversation_context

        + "\n\n"

        + context
    )

    # Generate AI answer
    final_answer = (
        generate_rag_answer(

            question,

            full_context
        )
    )

    # Store chat history
    CHAT_HISTORY.append({

        "question":
        question,

        "answer":
        final_answer
    })

    # Keep only recent chats
    if len(CHAT_HISTORY) > 5:

        CHAT_HISTORY.pop(0)

    return {

        "question":
        question,

        "answer":
        final_answer,

        "source":
        source
    }