import { useEffect, useRef } from "react";

import MessageBubble from "./MessageBubble";

function ChatWindow({ messages }) {

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({

            behavior: "smooth"
        });

    }, [messages]);

    return (

        <div className="h-full overflow-y-auto px-6 py-6">

            <div className="max-w-5xl mx-auto space-y-6">

                {
                    messages.length === 0 && (

                        <div className="h-[70vh] flex items-center justify-center">

                            <div className="text-center">

                                <h2 className="text-4xl font-bold text-white mb-4">

                                    Upload HR PDFs and start chatting

                                </h2>

                                <p className="text-gray-400 text-lg">

                                    Ask questions about onboarding,
                                    leave policy, HR rules, and more.

                                </p>

                            </div>

                        </div>
                    )
                }

                {
                    messages.map((message, index) => (

                        <MessageBubble
                            key={index}
                            message={message}
                        />
                    ))
                }

                <div ref={bottomRef}></div>

            </div>

        </div>
    );
}

export default ChatWindow;