LangChain Chatbot 🤖
A custom chatbot built with LangChain, FAISS, OpenAI API, and Flask to extract data from Brainlox Courses and provide relevant responses.

🚀 Features
✅ Extracts course data using LangChain URL loaders
✅ Embeddings stored in FAISS for efficient retrieval
✅ Flask REST API for easy integration
✅ Secure authentication using OpenAI API keys
✅ Handles user queries with an interactive chatbot

📂 Project Structure
graphql
Copy
Edit
📦 langchain-chatbot
 ┣ 📂 faiss_index/        # FAISS vector store directory
 ┣ 📜 ingest.py           # Script to load & process data
 ┣ 📜 query.py            # Chatbot query execution
 ┣ 📜 test.py             # Test script for chatbot responses
 ┣ 📜 requirements.txt    # Dependencies
 ┣ 📜 .gitignore          # Ignore unnecessary files
 ┗ 📜 README.md           # Project documentation
🔧 Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/SHUBHAG100520/longchain_chatbot.git
cd longchain_chatbot
2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up API Keys
Create a .env file and add:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
🚀 How to Run the Chatbot
1️⃣ Run Data Ingestion
sh
Copy
Edit
python ingest.py
This loads and indexes data into FAISS.

2️⃣ Start Chatbot
sh
Copy
Edit
python query.py
Now, ask questions and get responses!

💡 Example Usage
sh
Copy
Edit
Ask something: "What is LangChain?"
🤖 Chatbot: "LangChain is a framework for developing applications powered by LLMs."
📜 License
This project is open-source under the MIT License.
