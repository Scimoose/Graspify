# Import necessary modules and libraries
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain
import os
import gradio as gr

# Set the value of the OPENAI_API_KEY variable to the value of the environment variable "OPENAI_API_KEY"  # noqa: E501
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Supplying a persist_directory will store the embeddings on disk
persist_directory = 'db'

# Initialize the OpenAIEmbeddings module
embeddings = OpenAIEmbeddings()

# Load the persisted vector store from disk
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# Use the ChatVectorDBChain module to generate an answer to the user's input based on the loaded vector store and the OpenAI language model  # noqa: E501
MyOpenAI = OpenAI()
qa = ChatVectorDBChain.from_llm(MyOpenAI, vectordb)

def chatbot(input_text):
    # Add user input to message history
    chat_history.append("User: " + input_text)
    # Generate an answer to the user's input using the ChatVectorDBChain module
    response = qa({"question": input_text, "chat_history": message_history})
    print(response["answer"])
    # Add response to message history
    chat_history.append("Chatbot: " + response["answer"])
    # Return response
    return response["answer"] + "\n\n" + "\n".join(chat_history)

# Initialize message history
message_history = []
chat_history = []

if __name__ == "__main__":
    # Define Gradio interface
    iface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="Gradio Chat App", 
                        description="Enter a message to chat with the chatbot. Full message history will be displayed below.")

    # Run the interface
    iface.launch()
