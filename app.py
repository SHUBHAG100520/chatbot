import os
from flask import Flask, request, jsonify
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Langchain Chatbot API!"

@app.route("/chat", methods=["POST"])
def chat():
    """Handles user queries and retrieves responses using the FAISS vector store."""
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    # Load FAISS vector store
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.load_local("faiss_index", embeddings)

    # Use LLM to generate responses
    llm = OpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

    # Get chatbot response
    response = qa_chain.run(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)



