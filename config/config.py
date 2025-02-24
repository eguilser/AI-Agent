import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Cargar las variables de entorno
load_dotenv()

# Obtener API Key de Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "ia-agent"

# ⚠️ Verificar si el índice ya existe, en lugar de eliminarlo cada vez
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
