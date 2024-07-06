
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easy_rag",
    version="0.1.1",
    author="Tarun Baswa",
    author_email="tarunbaswa9059@gmail.com",
    description="A simple and secure RAG framework to rag any LLM model with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tarun0951/easy_rag",
    packages=find_packages(),
    classifiers=[
        
       
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "openai>=0.28.0",
        "chromadb>=0.3.0",
        "faiss-cpu>=1.7.0",
        "google-generativeai",
        "transformers>=4.0.0",
        "torch>=1.0.0",
    ],
    extras_require={
        "dev": ["pytest>=6.0", "black", "isort", "flake8"],
    },
)
