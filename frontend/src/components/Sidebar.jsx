function Sidebar() {

    return (

        <div className="w-72 bg-black border-r border-gray-800 p-6 hidden md:block">

            <h1 className="text-3xl font-bold text-white mb-10">

                HR AI

            </h1>

            <button
                className="w-full bg-white/10 hover:bg-white/20 transition-all border border-gray-700 text-white rounded-2xl p-4"
            >

                + New Chat

            </button>

            <div className="mt-10">

                <p className="text-gray-400 text-sm">

                    AI HR Knowledge Assistant

                </p>

            </div>

        </div>
    );
}

export default Sidebar;