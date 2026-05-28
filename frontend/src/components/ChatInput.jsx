import {

    useState

} from "react";


function ChatInput({

    onSend,

    loading

}) {

    const [

        question,

        setQuestion

    ] = useState("");

    const handleSend = () => {

        if (!question.trim()) {

            return;
        }

        onSend(question);

        setQuestion("");
    };

    const handleKeyDown = (e) => {

        if (

            e.key === "Enter"

            &&

            !e.shiftKey
        ) {

            e.preventDefault();

            handleSend();
        }
    };

    return (

        <div className="p-6 border-t border-gray-800 bg-black">

            <div className="flex gap-4">

                <textarea
                    rows={1}
                    value={question}
                    onChange={(e) =>
                        setQuestion(
                            e.target.value
                        )
                    }
                    onKeyDown={handleKeyDown}
                    placeholder="Ask something..."
                    className="flex-1 bg-white/10 border border-gray-700 text-white rounded-2xl p-4 outline-none resize-none"
                />

                <button
                    onClick={handleSend}
                    disabled={loading}
                    className="bg-gradient-to-r from-purple-500 to-blue-500 text-white px-8 rounded-2xl font-semibold hover:scale-105 transition-all duration-300 disabled:opacity-50"
                >

                    {

                        loading

                        ?

                        "Thinking..."

                        :

                        "Send"
                    }

                </button>

            </div>

        </div>
    );
}

export default ChatInput;