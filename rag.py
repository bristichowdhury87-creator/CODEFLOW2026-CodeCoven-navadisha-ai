from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.prompts import ChatPromptTemplate

PROMPT_TEMPLATE = """
You are Navadisha AI, a legal aid assistant for rural India.
You are talking to an illiterate farmer or rural worker who does not understand legal lanaguage.

Context from legal documents:
{context}

Their problem is:
{input}

Respond in this EXACT format using very simple words that even a 10 year old can understand.

PROBLEM UNDERSTOOD:
[One simple sentence summarizing the user's problem - no legal jargon]

YOUR RIGHTS
[One simple right they have - no legal jargon]

WHAT YOU MUST DO TODAY
Step 1:[Exact first action - where to go, who to meet]
Step 2:[Exact second action - what to say or bring]
Step 3:[Exact third action - what will happen next]

FREE HELP AVAILABLE:
- Place: [Nearest office they can walk to]
- Helpline: [Phone number they can call for free help]
- Cost: Zero rupees - completely free

REMEMBER:
[One encouraging sentence in sinple words]

If the user wrote in bengali, respond in bengali.
if the user wrote in hindi, respond in hindi.
Otherwise respond in simple English.
Always mix in simple Bengali or Hindi words to make it more relatable, even if the user wrote in English.
No legal terms. No complicated sentences.
Indian rural people should be able to understand and act on your advice without needing a lawyer.
"""

def load_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory="./legal_db", 
                         embedding_function=embedding_model)
    return vectorstore, embedding_model

def build_chain():
    vectorstore, embedding_model = load_vectorstore()
    dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    all_docs=vectorstore.get()
    from langchain_core.documents import Document
    docs_for_bm25=[
        Document(page_content=text)
        for text in all_docs["documents"]
    ]
    bm25_retriever = BM25Retriever.from_documents(docs_for_bm25)
    bm25_retriever.k=3
    hybrid_retriever=EnsembleRetriever(
    retrievers=[dense_retriever, bm25_retriever],
    weights=[0.5, 0.5]
    )
    llm=Ollama(model="gemma2:2b")
    prompt = ChatPromptTemplate.from_messages([
        ("system", PROMPT_TEMPLATE),
        ("human", "{input}"),
        ])
    document_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(hybrid_retriever, document_chain)
    return rag_chain

def ask_question(chain, question):
    response = chain.invoke({"input": question})
    return {
        "answer": response["answer"],
        "sources": [doc.metadata.get("source", "unknown") 
                    for doc in response["context"]]
    }
