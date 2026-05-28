import MessageBubble from "./MessageBubble";

function ChatWindow({

    messages

}) {

    return (

        <div className="flex-1 overflow-y-auto px-6 py-8 space-y-6">

            {

                messages.map(

                    (message, index) => (

                        <MessageBubble

                            key={index}

                            message={message}
                        />
                    )
                )
            }

        </div>
    );
}

export default ChatWindow;