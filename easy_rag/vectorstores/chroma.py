from typing import List
import chromadb
from .base import BaseVectorStore
from ..document import Document

class ChromaVectorStore(BaseVectorStore):
    def __init__(self, collection_name: str = "default_collection"):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(collection_name)

    def add_documents(self, documents: List[Document], embeddings: List[List[float]]):
        self.collection.add(
            embeddings=embeddings,
            documents=[doc.content for doc in documents],
            metadatas=[doc.metadata for doc in documents],
            ids=[str(i) for i in range(len(documents))]
        )

    def similarity_search(self, query_embedding: List[float], k: int = 4) -> List[Document]:
        results = self.collection.query(query_embeddings=[query_embedding], n_results=k)
        return [Document(content=doc, metadata=meta) 
                for doc, meta in zip(results['documents'][0], results['metadatas'][0])]