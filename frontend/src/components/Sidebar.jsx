function Sidebar({

    uploadedFiles,

    setMessages,

    setUploadedFiles,

    toggleSidebar,

    sidebarOpen
}) {

    const handleNewChat = () => {

        setMessages([]);
    };

    return (

        <>

            {
                sidebarOpen && (

                    <div className="w-80 bg-[#0b0b0b] border-r border-white/10 flex flex-col">

                        <div className="p-6 border-b border-white/10 flex justify-between items-center">

                            <button
                                onClick={handleNewChat}
                                className="flex-1 bg-gradient-to-r from-purple-500 to-blue-500 text-white py-3 rounded-2xl font-semibold hover:opacity-90 transition-all"
                            >

                                + New Chat

                            </button>

                            <button
                                onClick={toggleSidebar}
                                className="ml-4 text-gray-400 hover:text-white text-2xl"
                            >

                                ☰

                            </button>

                        </div>

                        <div className="p-6 overflow-y-auto">

                            <h2 className="text-white text-xl font-semibold mb-6">

                                Uploaded Documents

                            </h2>

                            <div className="space-y-4">

                                {
                                    uploadedFiles.length === 0 ? (

                                        <p className="text-gray-400 text-sm">

                                            No documents uploaded.

                                        </p>

                                    ) : (

                                        uploadedFiles.map((file, index) => (

                                            <div
                                                key={index}
                                                className="bg-white/5 border border-white/10 rounded-2xl p-4 text-gray-300 text-sm break-words"
                                            >

                                                {file}

                                            </div>
                                        ))
                                    )
                                }

                            </div>

                        </div>

                    </div>
                )
            }

        </>
    );
}

export default Sidebar;