from typing import List, Optional, Dict
from .document import Document
from .embeddings import get_embedding_model
from .vectorstores import get_vectorstore
from .llms import get_llm
from .utils.text_splitter import SimpleTextSplitter
from .retrievers.similarity import SimilarityRetriever
from .session import Session

class RAGFramework:
    def __init__(self,
                 embedding_provider: str,
                 vectorstore_provider: str,
                 llm_provider: str,
                 api_keys: Dict[str, str],
                 embedding_model: str = "default",
                 llm_model: str = "default",
                 system_prompt: Optional[str] = None,
                 text_splitter: Optional[SimpleTextSplitter] = None):
        
        self.session = Session()
        self.session.set_api_keys(api_keys)
        
        self.embedding = get_embedding_model(embedding_provider, self.session.get_api_key(embedding_provider), embedding_model)
        self.vectorstore = get_vectorstore(vectorstore_provider, self.session.get_api_key(vectorstore_provider))
        self.llm = get_llm(llm_provider, self.session.get_api_key(llm_provider), llm_model)
        
        self.system_prompt = system_prompt or self._default_system_prompt()
        self.text_splitter = text_splitter or SimpleTextSplitter()
        self.retriever = SimilarityRetriever(self.vectorstore, self.embedding)

    def _default_system_prompt(self) -> str:
        return ("You are a helpful AI assistant. Use the provided context to answer "
                "questions. If you're unsure or the answer isn't in the context, "
                "say you don't know.")

    def add_documents(self, documents: List[Document]):
        split_docs = []
        for doc in documents:
            chunks = self.text_splitter.split_text(doc.content)
            split_docs.extend([Document(chunk, doc.metadata) for chunk in chunks])
        
        embeddings = self.embedding.embed_batch([doc.content for doc in split_docs])
        self.vectorstore.add_documents(split_docs, embeddings)

    def query(self, query: str, k: int = 4) -> str:
        retrieved_docs = self.retriever.retrieve(query, k)
        context = "\n\n".join([doc.content for doc in retrieved_docs])
        
        prompt = f"{self.system_prompt}\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"
        
        return self.llm.generate(prompt)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.clear_api_keys()

class SecureRAGFramework:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __enter__(self):
        self.rag = RAGFramework(**self.kwargs)
        return self.rag

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.rag.session.clear_api_keys()