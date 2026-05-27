import axios from "axios";

import {
    useState
} from "react";

function PdfUpload() {

    const [
        loading,
        setLoading
    ] = useState(false);

    const [
        message,
        setMessage
    ] = useState("");

    const uploadPdf = async (
        event
    ) => {

        const files =
            event.target.files;

        if (!files.length) {

            return;
        }

        const formData =
            new FormData();

        for (
            let i = 0;
            i < files.length;
            i++
        ) {

            formData.append(
                "files",
                files[i]
            );
        }

        try {

            setLoading(true);

            setMessage(
                "Processing PDFs..."
            );

            const response =
                await axios.post(

                    "https://ai-research-assistant-z0mu.onrender.com/read-pdf",

                    formData,

                    {
                        headers: {
                            "Content-Type":
                            "multipart/form-data",
                        },
                    }
                );

            console.log(
                response.data
            );

            setMessage(
                "PDFs uploaded successfully."
            );

            setLoading(false);

        } catch (error) {

            console.log(error);

            setMessage(
                "PDF upload failed."
            );

            setLoading(false);
        }
    };

    return (

        <div className="mb-10">

            <h2 className="text-2xl font-semibold text-white mb-4">

                Upload PDFs

            </h2>

            <input
                type="file"
                multiple
                onChange={uploadPdf}
                className="w-full bg-white/10 text-white border border-gray-600 rounded-xl p-4 cursor-pointer"
            />

            <p className="text-gray-300 mt-4">

                {
                    loading
                    ? "Processing PDFs..."
                    : message
                }

            </p>

        </div>
    );
}

export default PdfUpload;