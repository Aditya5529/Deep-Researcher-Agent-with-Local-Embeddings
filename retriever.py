# src/retriever.py
from langchain_community.vectorstores import Chroma
from langchain_community.llms import LlamaCpp  # or you can later plug GPT4All
from langchain.chains import RetrievalQA

def load_retriever(persist_dir="indices/chroma"):
    # Reload persisted Chroma DB
    vectordb = Chroma(
        persist_directory=persist_dir,
        embedding_function=None  # embeddings not needed for retrieval
    )
    return vectordb.as_retriever(search_kwargs={"k": 5})

def build_qa_chain(model_path, persist_dir="indices/chroma"):
    retriever = load_retriever(persist_dir)

    # Local LLM (replace with your chosen .gguf model path)
    llm = LlamaCpp(
        model_path=model_path,
        n_ctx=2048,
        temperature=0.2,
        verbose=True
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    return qa
