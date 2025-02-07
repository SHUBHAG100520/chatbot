import os
os.environ["USER_AGENT"] = "Mozilla/5.0"
import sys
sys.stdout.reconfigure(encoding='utf-8')
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def ingest_data():
    """Extracts data from the website, creates embeddings, and stores in FAISS."""
    url = "https://brainlox.com/courses/category/technical"
    loader = WebBaseLoader(url)
    documents = loader.load()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # Generate embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(texts, embeddings)

    # Save FAISS vector store
    vectorstore.save_local("faiss_index")
    print("✅ Data successfully ingested and stored in FAISS!")

if __name__ == "__main__":
    ingest_data()
