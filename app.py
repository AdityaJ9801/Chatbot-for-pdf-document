import streamlit as st
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

os.environ['GOOGLE_API_KEY'] = 'AIzaSyD8uzXToT4I2ABs7qo_XiuKh8-L2nuWCEM'


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GooglePalmEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store


def get_conversational_chain(vector_store):
    llm = GooglePalm()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
    return conversation_chain


def user_input(user_question):
    with st.container():
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chatHistory = response['chat_history']
        file_contents = ""
        left , right = st.columns((2,1))
        with left:
            for i, message in enumerate(st.session_state.chatHistory):
                if i % 2 == 0:
                    st.write("Human:", message.content)
                else:
                    st.write("Bot:", message.content)
            st.success("Done !")
        with right:
            for message in st.session_state.chatHistory:
                file_contents += f"{message.content}\n"
            file_name = "Chat_History.txt"
            st.download_button("Download chat history👈", file_contents, file_name=file_name, mime="text/plain")


def summary(summarization):
    with st.container():
        file_contents = ''
        left , right = st.columns((2,1))
        with left:
            if summarization:
                response1 = st.session_state.conversation({'question': 'Retrieve one-line topics and their descriptors; create detailed, bulleted summaries for each topic.'})
                st.write("summary:\n", response1['answer'])
                st.success("Done !")
            else:
                response1 = {}

        with right:
            file_contents = response1.get('answer', '')
            file_name = "summarization_result.txt"
            st.download_button("Download summery👈", file_contents, file_name=file_name, mime="text/plain")


def main():
    st.set_page_config("Chat with Multiple PDFs")
    st.header("Chat with Multiple PDF 💬")
    st.write("---")
    with st.container():
        with st.sidebar:
            st.title("Settings")
            st.subheader("Upload your Documents")
            pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Process Button", accept_multiple_files=True)
            if st.button("Process"):
                with st.spinner("Processing"):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vector_store = get_vector_store(text_chunks)
                    st.session_state.conversation = get_conversational_chain(vector_store)
                    st.success("Done")
    with st.container():
        # Summarization Section
        st.subheader("PDF Summarization")
        st.write('Click on summary button to get summary on given uploaded file.')
        summarization = st.button("Summarize 👍")
        summary(summarization)

    st.write("#")
    st.write("---")

    with st.container():
        # Question Section
        st.subheader("PDF question-answer section")
        user_question = st.text_input("Ask a Question from the PDF Files")
        if "conversation" not in st.session_state:
            st.session_state.conversation = None
        if "chatHistory" not in st.session_state:
            st.session_state.chatHistory = None
        if user_question:
            user_input(user_question)


if __name__ == "__main__":
    main()
