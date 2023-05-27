# Import necessary modules and libraries
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
import os
import sys

# Load environment variables from .env file
load_dotenv()

# Set the value of the OPENAI_API_KEY variable to the value of the environment variable "OPENAI_API_KEY"  # noqa: E501
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

def add_pdf(document):
    """
    This function loads a PDF document, splits it into smaller chunks, generates embeddings for the text chunks using the OpenAIEmbeddings module and stores them in a Chroma vector store. 
    The vector store is then persisted to disk.
    
    Args:
    - document: a string representing the path to the PDF document to be loaded

    Returns:
    - None
    """  # noqa: E501
    
    # Embed and store the texts
    # Supplying a persist_directory will store the embeddings on disk
    persist_directory = 'db'

    # Load the text from a PDF file using the UnstructuredPDFLoader module
    loader = UnstructuredPDFLoader(document)
    documents = loader.load()

    # Split the loaded text into smaller chunks using the CharacterTextSplitter module
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Generate embeddings for the text chunks using the OpenAIEmbeddings module and store them in a Chroma vector store  # noqa: E501
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)

    # Persist the vector store to disk
    db.persist()
    db = None

if __name__ == "__main__":
    add_pdf(sys.argv[1])
    print("Done")
