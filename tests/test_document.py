import unittest
from easy_rag.document import Document

class TestDocument(unittest.TestCase):
    def test_document_creation(self):
        content = "Test content"
        metadata = {"source": "test"}
        doc = Document(content, metadata)
        self.assertEqual(doc.content, content)
        self.assertEqual(doc.metadata, metadata)

    def test_document_repr(self):
        doc = Document("Long content " * 10, {"source": "test"})
        repr_str = repr(doc)
        self.assertTrue(repr_str.startswith("Document(content=Long content Long content Long"))
        self.assertTrue(repr_str.endswith("..., metadata={'source': 'test'})"))

if __name__ == '__main__':
    unittest.main()