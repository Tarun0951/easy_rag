from typing import List
from transformers import AutoTokenizer, AutoModel
import torch
from .base import BaseEmbedding

class HuggingFaceEmbedding(BaseEmbedding):
    def __init__(self, api_key: str, model: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model, use_auth_token=api_key)
        self.model = AutoModel.from_pretrained(model, use_auth_token=api_key)

    def _embed_text(self, text: str) -> List[float]:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings[0].tolist()

    def embed(self, text: str) -> List[float]:
        return self._embed_text(text)

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        return [self._embed_text(text) for text in texts]