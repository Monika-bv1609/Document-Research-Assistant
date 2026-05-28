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
                "Uploading PDFs..."
            );

            const response =

                await axios.post(

                    "http://127.0.0.1:8000/read-pdf",
                    // "https://ai-research-assistant-z0mu.onrender.com/read-pdf",

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

        <div className="p-6 border-b border-gray-800 bg-black">

            <label
                className="block w-full cursor-pointer bg-white/10 hover:bg-white/20 border border-gray-700 text-white rounded-2xl p-6 text-center transition-all"
            >

                {

                    loading

                    ?

                    "Uploading..."

                    :

                    "Upload HR PDFs"
                }

                <input
                    type="file"
                    multiple
                    onChange={uploadPdf}
                    className="hidden"
                />

            </label>

            {

                message && (

                    <p className="text-gray-400 mt-4">

                        {message}

                    </p>
                )
            }

        </div>
    );
}

export default PdfUpload;