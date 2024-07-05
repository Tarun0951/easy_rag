from typing import Dict, Optional

class Document:
    def __init__(self, content: str, metadata: Optional[Dict] = None):
        self.content = content
        self.metadata = metadata or {}

    def __repr__(self):
        return f"Document(content={self.content[:50]}..., metadata={self.metadata})"