# Graspify - Your Chatbot Assistant
This is a LLM chatbot with chromaDB for document storage and GPT-3.5 for document analysis.

To get started, create a .env file and insert your OpenAI key.
> "OPENAI_API_KEY" = "your-key-here"

Then, install the required libraries with:
> pip install requirements.txt # TODO

# Usage
There are 3 files you should use.

Firstly, there is the add_document.py file. This one you can use to add documents to the database.
You can use it from the terminal, like this:
> python add_document.py document.pdf

As of now it only handles .pdf files, but will handle .doc and .txt files soon.

Then there is the main.py file. It uses gradio to abstract code and give a simple UI to the application. There you can flag conversations if you don't like those and if you find a bug you can attach the file that flagging generates. 
In the gradio app you can chat with the LLM, it also provides message history. 

Lastly, there is a Jupyter Notebook that will help you interact with the database should you wish to do so.
