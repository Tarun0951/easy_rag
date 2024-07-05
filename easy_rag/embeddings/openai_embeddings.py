import openai
from typing import List
from .base import BaseEmbedding

class OpenAIEmbedding(BaseEmbedding):
    def __init__(self, api_key: str, model: str = "text-embedding-ada-002"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def embed(self, text: str) -> List[float]:
        response = openai.Embedding.create(input=[text], model=self.model)
        return response['data'][0]['embedding']

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        response = openai.Embedding.create(input=texts, model=self.model)
        return [item['embedding'] for item in response['data']]