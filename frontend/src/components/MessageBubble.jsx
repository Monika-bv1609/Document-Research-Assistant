function MessageBubble({ message }) {

    return (

        <div
            className={`flex ${
                message.role === "user"
                ? "justify-end"
                : "justify-start"
            }`}
        >

            <div
                className={`max-w-2xl px-6 py-5 rounded-3xl ${
                    message.role === "user"
                    ? "bg-gradient-to-r from-purple-500 to-blue-500 text-white"
                    : "bg-white/10 border border-white/10 text-white"
                }`}
            >

                <p className="leading-8 whitespace-pre-wrap">

                    {message.content}

                </p>

                {
                    message.source && (

                        <p className="text-sm text-gray-400 mt-6">

                            Source: {message.source}

                        </p>
                    )
                }

            </div>

        </div>
    );
}

export default MessageBubble;