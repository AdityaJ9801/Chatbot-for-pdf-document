## Chatbot-for-pdf-document
<response>

  ![work flow diagram](https://github.com/AdityaJ9801/Chatbot-for-pdf-document/assets/124603391/dd60fc15-0d25-41b4-82db-64ccd1a822de)

Objective:
The code creates an interactive PDF chatbot using Streamlit, allowing users to upload PDFs, ask questions, and receive responses.

Key Features:
PDF Processing:

Extracts text from uploaded PDFs using PyPDF2.
Text Chunking:

Divides the extracted text into smaller chunks for efficient processing.
Text Embedding:

Converts text chunks into vectors using Google Palm embeddings.
Creates a vector store for efficient storage and retrieval.
Conversational Chain:

Initiates a conversational chain using LangChain's Google Palm model.
Utilizes a memory buffer to store chat history for context.
User Interaction:

Allows users to input questions through a Streamlit interface.
Conversation Display:

Displays the conversation history in a two-column layout.
Alternately shows messages from the user and the chatbot.
Download Functionality:

Enables users to download the entire chat history or summarization results.
Summarization:

Provides an option to summarize the content with one-line topics and descriptors.
Execution:
Run the script to launch the Streamlit web app.
Upload PDFs, ask questions, and explore chat history.

Dependencies:
Streamlit, PyPDF2, LangChain (text_splitter, embeddings, llms, vectorstores, chains, memory).
Usage:
Set your Google API key.
Run the script and interact with the PDF chatbot.
</response>
