from easy_rag import SecureRAGFramework, Document

# User-provided API keys
api_keys = {
   "openai": "",
    "gemini": "",
    
    "huggingface": ""

}

# Use the SecureRAGFramework in a with statement
with SecureRAGFramework(
    embedding_provider="huggingface",
    vectorstore_provider="chroma",
    llm_provider="gemini",
    api_keys=api_keys,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    llm_model="gemini-pro",
    system_prompt="You are a helpful assistant that answers questions based on the given context."
) as rag:

    # Add documents
    documents = [
        Document("paris", {"source": "geo.txt"}),
      
    ]
    rag.add_documents(documents)

    # Query the RAG system
    query = "give few lines about paris and its specialities  in 3 words ?"
    response = rag.query(query)
    print(f"Query: {query}")
    print(f"Response: {response}")

