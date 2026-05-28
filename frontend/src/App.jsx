import {

    useState

} from "react";

import axios from "axios";

import Sidebar from "./components/Sidebar";

import PdfUpload from "./components/PdfUpload";

import ChatWindow from "./components/ChatWindow";

import ChatInput from "./components/ChatInput";


function App() {

    const [

        messages,

        setMessages

    ] = useState([]);

    const [

        loading,

        setLoading

    ] = useState(false);

    const sendMessage = async (

        question
    ) => {

        // Add user message
        setMessages((prev) => [

            ...prev,

            {
                role: "user",

                content: question
            }
        ]);

        try {

            setLoading(true);

            const response = await axios.post(

                "http://127.0.0.1:8000/ask-pdf",

                {},

                {
                    params: {
                        question: question
                    }
                }
            );

            // const response = await axios.post(

            //    "http://127.0.0.1:8000/ask-pdf",

            //     // `https://ai-research-assistant-z0mu.onrender.com/ask-pdf?question=${question}`
            // );

            // Add AI response
            setMessages((prev) => [

                ...prev,

                {
                    role: "assistant",

                    content:
                    response.data.answer,

                    source:
                    response.data.source
                }
            ]);

        } catch (error) {

            console.log(error);

            setMessages((prev) => [

                ...prev,

                {
                    role: "assistant",

                    content:
                    "Something went wrong."
                }
            ]);

        } finally {

            setLoading(false);
        }
    };

    return (

        <div className="h-screen bg-gradient-to-br from-gray-900 via-black to-gray-800 flex overflow-hidden">

            {/* Sidebar */}
            <Sidebar />

            {/* Main Chat Area */}
            <div className="flex-1 flex flex-col">

                {/* Header */}
                <div className="border-b border-gray-800 p-6 bg-black">

                    <h1 className="text-4xl font-bold text-white">

                        HR AI Assistant

                    </h1>

                    <p className="text-gray-400 mt-2">

                        Chat with your HR documents using AI

                    </p>

                </div>

                {/* PDF Upload */}
                <PdfUpload />

                {/* Chat Window */}
                <ChatWindow messages={messages} />

                {/* Chat Input */}
                <ChatInput

                    onSend={sendMessage}

                    loading={loading}
                />

            </div>

        </div>
    );
}

export default App;