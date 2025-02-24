from langchain_core.embeddings import Embeddings
from sentence_transformers import SentenceTransformer

class HuggingFaceEmbeddings(Embeddings):
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return [self.model.encode(text).tolist() for text in texts]

    def embed_query(self, text):
        return self.model.encode(text).tolist()
