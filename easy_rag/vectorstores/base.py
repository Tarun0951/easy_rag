from abc import ABC, abstractmethod
from typing import List
from ..document import Document

class BaseVectorStore(ABC):
    @abstractmethod
    def add_documents(self, documents: List[Document], embeddings: List[List[float]]):
        pass

    @abstractmethod
    def similarity_search(self, query_embedding: List[float], k: int = 4) -> List[Document]:
        pass