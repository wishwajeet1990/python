from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# ------------ STEP 1: Load Documents -------------
def load_documents():
    docs = []

    # load PDFs
    pdf_loader = PyPDFLoader("Simple_RAG\data\Wishwajeet.pdf")
    docs.extend(pdf_loader.load())

    # Example for text files
    # text_loader = TextLoader("data/file.txt")
    # docs.extend(text_loader.load())

    return docs

# ------------ STEP 2: Split into small chunks -------------
def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(docs)

# ------------ STEP 3: Embed & store in FAISS -------------
def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

# ------------ STEP 4: Load a small FREE LLM -------------
def load_llm():
    model_name = "tiiuae/falcon-7b-instruct"  # any HF model
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=256
    )
    llm = HuggingFacePipeline(pipeline=pipe)
    return llm

# ------------ STEP 5: RAG Answering -------------
def answer_question(query, vectorstore, llm):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
    Use ONLY the context below to answer the question.

    CONTEXT:
    {context}

    QUESTION: {query}

    ANSWER:
    """

    return llm(prompt)

# ------------ MAIN DRIVER CODE -------------
if __name__ == "__main__":
    print("Loading documents...")
    docs = load_documents()

    print("Splitting...")
    chunks = split_documents(docs)

    print("Creating vector DB...")
    vectorstore = create_vector_store(chunks)

    print("Loading LLM...")
    llm = load_llm()

    print("Ready!")
    while True:
        query = input("\nAsk something: ")
        answer = answer_question(query, vectorstore, llm)
        print("\nANSWER:")
        print(answer)
