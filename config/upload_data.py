import os
import sys
# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from dotenv import load_dotenv
from langchain_pinecone import Pinecone
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from config import pc, index_name
from embeddings.huggingface_embeddings import HuggingFaceEmbeddings # Importamos la clase de embeddings

# Cargar variables de entorno
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

if not HUGGINGFACE_API_KEY:
    raise ValueError("❌ ERROR: No se encontró la API Key de Hugging Face en el archivo .env")

# Modelo de Hugging Face para generación de texto
MODEL = "HuggingFaceH4/zephyr-7b-beta"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

# Función para hacer consultas a Hugging Face
def query_huggingface(text):
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": text, "parameters": {"max_new_tokens": 100}})
        response_data = response.json()
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error al consultar Hugging Face: {e}")
        return None

# ✅ Verificar si el índice ya existe en Pinecone
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # Dimensión correcta para embeddings de Hugging Face
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")  # Región permitida
    )
    print(f"✅ Nuevo índice '{index_name}' creado en Pinecone con dimensión 384 en us-east-1.")
else:
    print(f"✅ Índice '{index_name}' ya existe. No se ha eliminado.")

# Conectar con el índice de Pinecone usando embeddings de Hugging Face
index = pc.Index(index_name)
embedding_model = HuggingFaceEmbeddings()
vectorstore = Pinecone.from_existing_index(index_name=index_name, embedding=embedding_model)

# Cargar documentos desde un archivo
loader = TextLoader(os.path.join(os.path.dirname(__file__), "../data/data.txt"), encoding='utf-8') # Ruta correcta al archivo data.txt en la carpeta data
documents = loader.load()

# Dividir en fragmentos pequeños para indexar
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Insertar en la base vectorial con embeddings personalizados
vectorstore.add_documents(docs)
print("✅ Datos guardados en Pinecone")

# Realizar una consulta en Pinecone y Hugging Face
query = "¿Qué es la inteligencia artificial?"
similar_docs = vectorstore.similarity_search(query, k=3)

# Mostrar resultados de Pinecone
print("\n📌 Documentos más similares en Pinecone:")
for doc in similar_docs:
    print(f"- {doc.page_content}\n")

# Hacer consulta a Hugging Face
response = query_huggingface(query)

# Mostrar respuesta de Hugging Face
print("\n📌 Respuesta de Hugging Face:")
if response and isinstance(response, list) and len(response) > 0 and "generated_text" in response[0]:
    print(response[0]["generated_text"])
else:
    print("⚠️ No se encontró 'generated_text' en la respuesta o la API devolvió un error.")

# Probar la búsqueda directamente en upload_data.py
print("\n📌 Prueba directa de búsqueda en Pinecone:")
test_query = "¿Qué es la inteligencia artificial?"
test_docs = vectorstore.similarity_search(test_query, k=3)

for doc in test_docs:
    print(f"- {doc.page_content}\n")
