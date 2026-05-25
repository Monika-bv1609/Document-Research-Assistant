import axios from "axios";

import {
    useState
} from "react";

function AskQuestion() {

    const [
        question,
        setQuestion
    ] = useState("");

    const [
        answer,
        setAnswer
    ] = useState("");

    const [
        loading,
        setLoading
    ] = useState(false);

    const askQuestion = async () => {

        if (!question) {
            return;
        }

        try {

            setLoading(true);

            setAnswer(
                "AI is analyzing document..."
            );

            const formData = new FormData();

            formData.append(
                "question",
                question
            );

            const response = await axios.post(
                "https://ai-research-assistant-z0mu.onrender.com/ask-pdf",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            setAnswer(
                response.data.answer
            );

        } catch (error) {

            console.log(
                error.response?.data
            );

            setAnswer(
                "Question failed."
            );

        } finally {

            setLoading(false);
        }
    };

    return (

        <div>

            <h2 className="text-2xl font-semibold text-white mb-4">

                Ask Question

            </h2>

            <div className="flex gap-4">

                <input
                    type="text"
                    value={question}
                    placeholder="Ask something about the PDF..."
                    onChange={(e) =>
                        setQuestion(
                            e.target.value
                        )
                    }
                    className="flex-1 bg-white/10 border border-gray-600 text-white placeholder-gray-400 rounded-xl p-4 outline-none"
                />

                <button
                    onClick={askQuestion}
                    disabled={loading}
                    className="bg-gradient-to-r from-purple-500 to-blue-500 hover:scale-105 transition-all duration-300 text-white px-8 rounded-xl font-semibold disabled:opacity-50"
                >
                    {
                        loading
                        ? "Thinking..."
                        : "Ask"
                    }

                </button>

            </div>

            <div className="mt-8 bg-white/10 border border-gray-700 p-6 rounded-2xl">

                <h3 className="text-2xl font-semibold text-white mb-4">

                    Answer

                </h3>

                <p className="text-gray-200 leading-8 whitespace-pre-wrap">

                    {answer || "AI response will appear here..."}

                </p>

            </div>

        </div>
    );
}

export default AskQuestion;

