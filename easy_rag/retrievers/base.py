from abc import ABC, abstractmethod
from typing import List
from ..document import Document

class BaseRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str, k: int = 4) -> List[Document]:
        pass