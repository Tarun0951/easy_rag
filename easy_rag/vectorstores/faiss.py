from typing import List
import faiss
import numpy as np
from .base import BaseVectorStore
from ..document import Document

class FAISSVectorStore(BaseVectorStore):
    def __init__(self):
        self.index = None
        self.documents = []

    def add_documents(self, documents: List[Document], embeddings: List[List[float]]):
        if self.index is None:
            self.index = faiss.IndexFlatL2(len(embeddings[0]))
        
        self.index.add(np.array(embeddings, dtype=np.float32))
        self.documents.extend(documents)

    def similarity_search(self, query_embedding: List[float], k: int = 4) -> List[Document]:
        D, I = self.index.search(np.array([query_embedding], dtype=np.float32), k)
        return [self.documents[i] for i in I[0]]