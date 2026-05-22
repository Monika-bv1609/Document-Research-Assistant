def chunk_text(
    text: str
):

    chunks = []

    # Split by lines
    lines = text.split("\n")

    current_chunk = ""

    for line in lines:

        line = line.strip()

        if not line:

            continue

        # Build meaningful chunk
        current_chunk += (
            line + "\n"
        )

        # Save chunk after few lines
        if len(current_chunk) > 200:

            chunks.append(
                current_chunk
            )

            current_chunk = ""

    # Add remaining chunk
    if current_chunk:

        chunks.append(
            current_chunk
        )

    return chunks