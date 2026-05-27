from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def chunk_text(
    text: str
):

    text_splitter = (
        RecursiveCharacterTextSplitter(

            chunk_size=300,

            chunk_overlap=50
        )
    )

    chunks = (
        text_splitter.split_text(
            text
        )
    )

    return chunks