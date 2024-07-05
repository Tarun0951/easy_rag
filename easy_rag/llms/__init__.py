from .base import BaseLLM
from .openai import OpenAILLM
from .gemini import GeminiLLM

def get_llm(provider: str, api_key: str, model: str = "default") -> BaseLLM:
    if provider == "openai":
        return OpenAILLM(api_key, model)
    elif provider == "gemini":
        return GeminiLLM(api_key, model)
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")