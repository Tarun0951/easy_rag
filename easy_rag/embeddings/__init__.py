from .base import BaseEmbedding
from .openai_embeddings import OpenAIEmbedding
from .huggingface_embeddings import HuggingFaceEmbedding

def get_embedding_model(provider: str, api_key: str, model: str = "default") -> BaseEmbedding:
    if provider == "openai":
        return OpenAIEmbedding(api_key, model)
    elif provider == "huggingface":
        return HuggingFaceEmbedding(api_key, model)
    else:
        raise ValueError(f"Unsupported embedding provider: {provider}")