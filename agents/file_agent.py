import os
import sys
# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_pinecone import Pinecone
from embeddings.huggingface_embeddings import HuggingFaceEmbeddings
from config.config import pc, index_name

# Cargar el modelo de embeddings
embedding_model = HuggingFaceEmbeddings()

# Conectar con el índice existente de Pinecone
print(f"🔗 Conectando al índice '{index_name}' en Pinecone...")
vectorstore = Pinecone.from_existing_index(index_name=index_name, embedding=embedding_model)

# Función para realizar una búsqueda en archivos locales
def search_in_files(query: str, top_k: int = 3):
    print(f'🔍 Realizando búsqueda para: "{query}"')
    similar_docs = vectorstore.similarity_search(query, k=top_k)
    
    if not similar_docs:
        print('⚠️ No se encontraron documentos similares.')
        return
    
    print("\n📄 Documentos más similares encontrados:")
    for doc in similar_docs:
        print(f"- {doc.page_content}\n")

# Ejemplo de uso
if __name__ == '__main__':
    query = "¿Qué es la inteligencia artificial?"
    search_in_files(query)
