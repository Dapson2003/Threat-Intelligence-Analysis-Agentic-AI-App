from langchain.schema import Document
from rag.rag_vector_db import create_vectorstore, load_vectorstore

class RagVectorStore:
    def __init__(self):
        self.vectorstore = None

    def ingest_text_file(self, filepath: str):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        doc = Document(page_content=content)
        self.vectorstore = create_vectorstore([doc])

    def query(self, query: str, k: int = 3):
        if not self.vectorstore:
            self.vectorstore = load_vectorstore()
        return self.vectorstore.similarity_search(query, k=k)
