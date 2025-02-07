import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import sys

sys.stdout.reconfigure(encoding="utf-8")  # Force UTF-8 output

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("❌ ERROR: OPENAI_API_KEY is missing from .env file!")
    exit()

def ask_question(query):
    """Queries the chatbot and returns a response."""
    print("🔹 Initializing Embeddings...")  
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    print("🔹 Loading FAISS vector store...")  
    try:
        vectorstore = FAISS.load_local("faiss_index", embeddings)
    except Exception as e:
        print("❌ ERROR: FAISS failed to load!", str(e))
        return "Error: FAISS index not found."

    print("🔹 Setting up LLM model...")  
    llm = OpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

    print("🔹 Running Query...")  
    return qa_chain.run(query)

if __name__ == "__main__":
    while True:
        try:
            query = input("Ask something: ")  # FIXED INPUT

            print("You typed:", query)

            if query.lower() == "exit":
                break
            response = ask_question(query)
            print("🤖 Chatbot:", response)
        except KeyboardInterrupt:
            print("\n👋 Exiting Chatbot...")
            break
        except Exception as e:
            print("❌ ERROR:", str(e))
