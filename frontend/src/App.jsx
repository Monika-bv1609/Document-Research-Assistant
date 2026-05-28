import { useRef, useState } from "react";

import Sidebar from "./components/Sidebar";

import ChatWindow from "./components/ChatWindow";

import ChatInput from "./components/ChatInput";

function App() {

    const [messages, setMessages] = useState([]);

    const [uploadedFiles, setUploadedFiles] = useState([]);

    const [sidebarOpen, setSidebarOpen] = useState(true);

    const fileInputRef = useRef(null);

    const handleUploadClick = () => {

        fileInputRef.current.click();
    };

    const handleSidebarToggle = () => {

        setSidebarOpen(!sidebarOpen);
    };

    return (

        <div className="h-screen bg-black flex overflow-hidden">

            <Sidebar

                uploadedFiles={uploadedFiles}

                setMessages={setMessages}

                setUploadedFiles={setUploadedFiles}

                toggleSidebar={handleSidebarToggle}

                sidebarOpen={sidebarOpen}
            />

            <div className="flex-1 flex flex-col">

                <div className="p-6 border-b border-white/10 flex items-center">

                    {
                        !sidebarOpen && (

                            <button
                                onClick={handleSidebarToggle}
                                className="text-white text-3xl mr-6"
                            >

                                ☰

                            </button>
                        )
                    }

                    <div>

                        <h1 className="text-5xl font-bold text-white">

                            HR AI Assistant

                        </h1>

                        <p className="text-gray-400 mt-2 text-lg">

                            Chat with your HR documents using AI

                        </p>

                    </div>

                </div>

                <ChatWindow
                    messages={messages}
                />

                <ChatInput

                    messages={messages}

                    setMessages={setMessages}

                    fileInputRef={fileInputRef}

                    setUploadedFiles={setUploadedFiles}
                />

            </div>

        </div>
    );
}

export default App;