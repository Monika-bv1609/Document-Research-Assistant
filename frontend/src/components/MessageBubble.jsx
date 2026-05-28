function MessageBubble({

    message

}) {

    const isUser =

        message.role === "user";

    return (

        <div
            className={`flex ${
                isUser
                ? "justify-end"
                : "justify-start"
            }`}
        >

            <div
                className={`max-w-3xl px-6 py-4 rounded-3xl shadow-lg ${
                    isUser
                    ? "bg-gradient-to-r from-purple-500 to-blue-500 text-white"
                    : "bg-white/10 border border-gray-700 text-gray-200"
                }`}
            >

                <p className="leading-8 whitespace-pre-wrap">

                    {message.content}

                </p>

                {

                    !isUser && message.source && (

                        <p className="text-sm text-gray-400 mt-4">

                            Source:
                            {" "}
                            {message.source}

                        </p>
                    )
                }

            </div>

        </div>
    );
}

export default MessageBubble;