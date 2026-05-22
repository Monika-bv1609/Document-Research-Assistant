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

        const file = event.target.files[0];

        if (!file) {

            return;
        }

        const formData = new FormData();

        formData.append(
            "file",
            file
        );

        try {

            setLoading(true);

            setMessage(
                "Processing PDF..."
            );

            const response =
                await axios.post(

                    "http://127.0.0.1:8000/read-pdf",

                    formData
                );

            setMessage(
                response.data.message
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

                Upload PDF

            </h2>

            <input
                type="file"
                onChange={uploadPdf}
                className="w-full bg-white/10 text-white border border-gray-600 rounded-xl p-4 cursor-pointer"
            />

            <p className="text-gray-300 mt-4">

                {
                    loading
                    ? "Processing PDF..."
                    : message
                }

            </p>

        </div>
    );
}

export default PdfUpload;