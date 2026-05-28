import axios from "axios";

function PdfUpload({

    setUploadedFiles,

    setMessages
}) {

    const uploadPdf = async (event) => {

        const files = event.target.files;

        if (!files.length) {

            return;
        }

        const formData = new FormData();

        for (let file of files) {

            formData.append(
                "files",
                file
            );
        }

        try {

            const response = await axios.post(

                "http://127.0.0.1:8000/read-pdf",

                formData
            );

            const uploaded = response.data.uploaded_files;

            const fileNames = uploaded.map(

                (file) => file.filename
            );

            setUploadedFiles(fileNames);

            setMessages((prev) => [

                ...prev,

                {
                    role: "assistant",

                    content:
                    "PDFs uploaded successfully."
                }
            ]);

        } catch (error) {

            console.log(error);
        }
    };

    return (

        <div className="p-4 border-b border-white/10">

            <label className="flex items-center justify-center h-20 rounded-2xl border border-white/10 bg-white/5 text-white text-xl cursor-pointer hover:bg-white/10 transition-all">

                Upload HR PDFs

                <input
                    type="file"
                    multiple
                    hidden
                    onChange={uploadPdf}
                />

            </label>

        </div>
    );
}

export default PdfUpload;