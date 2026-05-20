from pypdf import PdfReader


def read_pdf(
    file_path: str
):

    try:

        # Open PDF
        reader = PdfReader(
            file_path
        )

        text = ""

        # Read all pages
        for page in reader.pages:

            text += (
                page.extract_text()
                + "\n"
            )

        return text

    except Exception as e:

        print(e)

        return (
            "PDF reading failed."
        )