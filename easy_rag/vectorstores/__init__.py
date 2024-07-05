from .base import BaseVectorStore
from .chroma import ChromaVectorStore
from .faiss import FAISSVectorStore

def get_vectorstore(provider: str, api_key: str = None) -> BaseVectorStore:
    if provider == "chroma":
        return ChromaVectorStore()
    elif provider == "faiss":
        return FAISSVectorStore()
    else:
        raise ValueError(f"Unsupported vector store provider: {provider}")