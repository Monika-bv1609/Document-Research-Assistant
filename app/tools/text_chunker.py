def chunk_text(
    text: str,
    chunk_size: int = 500
):

    chunks = []

    # Split text into chunks
    for index in range(

        0,
        len(text),
        chunk_size
    ):

        chunk = text[
            index:index + chunk_size
        ]

        chunks.append(
            chunk
        )

    return chunks