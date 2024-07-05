from typing import List
from .base import BaseRetriever
from ..vectorstores.base import BaseVectorStore
from ..embeddings.base import BaseEmbedding
from ..document import Document

class SimilarityRetriever(BaseRetriever):
    def __init__(self, vectorstore: BaseVectorStore, embedding: BaseEmbedding):
        self.vectorstore = vectorstore
        self.embedding = embedding

    def retrieve(self, query: str, k: int = 4) -> List[Document]:
        query_embedding = self.embedding.embed(query)
        return self.vectorstore.similarity_search(query_embedding, k)