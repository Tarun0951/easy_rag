# EasyRAG: A Simple and Secure RAG Framework

EasyRAG is a Python library that simplifies the implementation of Retrieval-Augmented Generation (RAG) systems. It provides a modular and extensible framework for building RAG applications with various embedding models, vector stores, and language models.

## Features

- Secure handling of API keys
- Support for multiple embedding providers (OpenAI, HuggingFace)
- Integration with various vector stores (Chroma, FAISS)
- Flexible LLM support (OpenAI, Google Gemini)
- Easy document management
- Configurable text splitting

## Installation

```bash
pip install easy_rag
```

## Getting Started

Here is a basic example to get started using the EasyRAG framework:

```python
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
        Document("Paris is the capital of France, known for its art, fashion, and culture.", {"source": "geo.txt"}),
    ]
    rag.add_documents(documents)

    # Query the RAG system
    query = "Give a few lines about Paris and its specialities in 3 words."
    response = rag.query(query)
    print(f"Query: {query}")
    print(f"Response: {response}")
```

This example uses the `gemini` LLM with the `sentence-transformers/all-MiniLM-L6-v2` embedding model. You can customize it with OpenAI or any other supported provider based on your convenience. The framework ensures secure handling of API keys and provides flexibility in choosing different models and vector stores.

## Customization

You can easily customize the framework to use different embedding providers, vector stores, and language models. Here is an example using OpenAI's embedding model and LLM:

```python
from easy_rag import SecureRAGFramework, Document

# User-provided API keys
api_keys = {
    "openai": "your_openai_api_key",
    "gemini": "",
    "huggingface": ""
}

# Use the SecureRAGFramework in a with statement
with SecureRAGFramework(
    embedding_provider="openai",
    vectorstore_provider="faiss",
    llm_provider="openai",
    api_keys=api_keys,
    embedding_model="text-embedding-ada-002",
    llm_model="text-davinci-003",
    system_prompt="You are a helpful assistant that answers questions based on the given context."
) as rag:

    # Add documents
    documents = [
        Document("Paris is the capital of France, known for its art, fashion, and culture.", {"source": "geo.txt"}),
    ]
    rag.add_documents(documents)

    # Query the RAG system
    query = "Give a few lines about Paris and its specialities in 3 words."
    response = rag.query(query)
    print(f"Query: {query}")
    print(f"Response: {response}")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to improve EasyRAG. Please fork the repository and submit pull requests.

