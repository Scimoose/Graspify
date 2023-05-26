# Import necessary modules and libraries
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain
import os
import gradio as gr

# Set the value of the OPENAI_API_KEY variable to the value of the environment variable "OPENAI_API_KEY"  # noqa: E501
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Supplying a persist_directory will store the embeddings on disk. This will create a new folder in the direcotry where this script is located  # noqa: E501
persist_directory = 'db'

# Initialize the OpenAIEmbeddings module
embeddings = OpenAIEmbeddings()

# Load the vector store from disk
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# Use the ChatVectorDBChain module to generate an answer to the user's input based on the loaded vector store and the OpenAI language model  # noqa: E501
MyOpenAI = OpenAI()
qa = ChatVectorDBChain.from_llm(MyOpenAI, vectordb)

def chatbot(your_input):
    # Add user input to message history
    chat_history.append("User: " + your_input)
    # Generate an answer to the user's input using the ChatVectorDBChain module
    response = qa({"question": your_input, "chat_history": message_history})
    # Add response to message history
    chat_history.append("Chatbot: " + response["answer"])
    # Return response
    return [response["answer"], "\n".join(chat_history)]  # noqa: E501

"""
Initialize message history and chat history. These must be separate, 
Message history is used by the ChatVectorDBChain module to generate an answer to the user's input
Chat history is used to display the full chat history to the user
"""  # noqa: E501

message_history = []
chat_history = []

if __name__ == "__main__":
    # Define Gradio interface and its boxes
    text = gr.components.Textbox(lines=1, label="Message")
    textbox = gr.components.Textbox(lines=1, label="Answer")
    history = gr.components.Textbox(lines=10, label="Chat History")

    iface = gr.Interface(fn=chatbot, inputs=text, outputs=[textbox, history], title="Graspify - Document Chat Assistant",   # noqa: E501
                        description="Enter a message to chat with the chatbot. Full message history will be displayed below.")  # noqa: E501

    # Run the interface
    iface.launch()
