# PDF Chatbot with Streamlit and LangChain


https://github.com/AdityaJ9801/Chatbot-for-pdf-document/assets/124603391/d2b36ae0-a4ec-4479-a34a-dde7f53b1bda


## Overview

This repository hosts a versatile PDF chatbot built using Streamlit and LangChain. The chatbot allows users to interact with uploaded PDF files, ask questions, and receive context-aware responses. The project leverages PyPDF2 for PDF text extraction, LangChain for efficient text processing and conversation handling, and Streamlit for the user interface.

![work flow diagram](https://github.com/AdityaJ9801/Chatbot-for-pdf-document/assets/124603391/f71d79cf-6829-49b5-835d-a41ba4623cbe)

## Features

- **PDF Processing:**
  - Utilizes PyPDF2 to extract text from uploaded PDFs.

- **Text Processing:**
  - Employs LangChain's text splitter for efficient chunking.

- **Text Embedding:**
  - Applies Google Palm embeddings for vectorization.

- **Conversational Chain:**
  - Establishes a conversational chain with LangChain's Google Palm model.
  - Implements memory management for enhanced conversation context.

- **User Interface:**
  - Streamlit-based interface for seamless user interactions.

- **Conversation History:**
  - Displays conversation history in a two-column layout.

- **Download Functionality:**
  - Allows users to download the entire chat history.

- **Summarization:**
  - Provides an option for content summarization.

## Usage

1. Set up your Google API key in the environment variable.
   ```bash
   export GOOGLE_API_KEY='YOUR_API_KEY'

## Run the script to launch the Streamlit application.
    ```bash
    - streamlit run app.py
