import axios from "axios";

import { useState } from "react";

function ChatInput({

    setMessages,

    fileInputRef,

    setUploadedFiles
}) {

    const [input, setInput] = useState("");

    const handleSend = async () => {

        if (!input.trim()) {

            return;
        }

        const userMessage = {

            role: "user",

            content: input
        };

        setMessages((prev) => [

            ...prev,

            userMessage
        ]);

        const question = input;

        setInput("");

        try {

            const response = await axios.post(

                "http://127.0.0.1:8000/ask-pdf",

                {},

                {
                    params: {
                        question
                    }
                }
            );

            const aiMessage = {

                role: "assistant",

                content:
                response.data.answer,

                source:
                response.data.source
            };

            setMessages((prev) => [

                ...prev,

                aiMessage
            ]);

        } catch (error) {

            console.log(error);
        }
    };

    const handleFileUpload = async (event) => {

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

        <div className="p-6 border-t border-white/10 flex gap-4 items-center">

            <input
                type="file"
                multiple
                hidden
                ref={fileInputRef}
                onChange={handleFileUpload}
            />

            <button
                onClick={() =>
                    fileInputRef.current.click()
                }
                className="w-14 h-14 rounded-2xl bg-white/5 border border-white/10 text-white text-3xl flex items-center justify-center hover:bg-white/10 transition-all"
            >

                +

            </button>

            <input
                type="text"
                value={input}
                placeholder="Ask something..."
                onChange={(e) =>
                    setInput(e.target.value)
                }
                onKeyDown={(e) => {

                    if (e.key === "Enter") {

                        handleSend();
                    }
                }}
                className="flex-1 h-14 bg-white/5 border border-white/10 rounded-2xl px-6 text-white outline-none"
            />

            <button
                onClick={handleSend}
                className="px-10 h-14 rounded-2xl bg-gradient-to-r from-purple-500 to-blue-500 text-white font-semibold"
            >

                Send

            </button>

        </div>
    );
}

export default ChatInput;