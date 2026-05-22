import PdfUpload from "./components/PdfUpload";

import AskQuestion from "./components/AskQuestion";

function App() {

    return (

        <div className="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-800 flex justify-center items-center p-6">

            <div className="bg-white/10 backdrop-blur-lg border border-white/20 p-10 rounded-3xl shadow-2xl w-[800px]">

                <h1 className="text-6xl font-extrabold text-center text-white mb-3">

                    AI PDF Assistant

                </h1>

                <p className="text-center text-gray-300 mb-12">

                    Upload PDFs and chat with your documents using AI

                </p>

                <PdfUpload />

                <AskQuestion />

            </div>

        </div>
    );
}

export default App;