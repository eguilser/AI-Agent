import os
import sys
import re
import time
from dotenv import load_dotenv

# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importar los agentes de búsqueda locales y web
from agents.file_agent import search_in_files
from agents.web_agent import search_online
from agents.history_manager import HistoryManager
from agents.cache_manager import CacheManager

# Cargar las variables de entorno
load_dotenv()

# Inicializar el historial y el cache
history_manager = HistoryManager()
cache_manager = CacheManager()

# Función para normalizar y limpiar las consultas
def preprocess_query(query: str) -> str:
    query = query.lower().strip()  # Pasar a minúsculas y eliminar espacios
    query = re.sub(r'\s+', ' ', query)  # Reemplazar espacios múltiples con uno solo
    query = re.sub(r'[^\w\s¿?]', '', query)  # Eliminar caracteres especiales excepto signos de pregunta
    return query

# Función del agente unificado mejorado
def unified_search(query: str, local_first: bool = True, top_k: int = 3, search_timeout: int = 5):
    """
    Realiza una búsqueda en archivos locales y en la web de manera eficiente.
    
    :param query: La consulta de búsqueda.
    :param local_first: Si es True, se busca primero en archivos locales.
    :param top_k: Número de resultados a mostrar.
    :param search_timeout: Tiempo máximo para la búsqueda en la web (en segundos).
    """
    query = preprocess_query(query)
    print(f"\n🤖 Realizando búsqueda unificada para: \"{query}\"\n")

    # Comprobar si la consulta está en la caché
    cached_result = cache_manager.get_from_cache(query)
    if cached_result:
        print("\n📦 Resultado en caché encontrado:")
        print(cached_result)
        return

    # Búsqueda en archivos locales
    if local_first:
        print("🔍 Búsqueda en archivos locales...")
        search_in_files(query, top_k)

    # Búsqueda en la web con límite de tiempo
    print("\n🌐 Búsqueda en la web...")
    try:
        start_time = time.time()
        search_online(query, top_k)
        elapsed_time = time.time() - start_time
        if elapsed_time > search_timeout:
            print("⏱️ La búsqueda en la web tomó demasiado tiempo y fue detenida.")
    except Exception as e:
        print(f"⚠️ Error durante la búsqueda en la web: {e}")
    
    # Guardar la consulta en el historial
    history_manager.add_query(query)

    # Cachear el resultado para futuras consultas
    cache_manager.add_to_cache(query, f"Resultados para: {query}")

# Ejemplo de uso en modo conversacional
if __name__ == '__main__':
    print("\n🧠 Bienvenido al Agente de IA Unificado 🧠")
    while True:
        query = input("\n🔍 Introduce tu consulta (o escribe 'salir' para terminar, 'historial' para ver consultas anteriores): ").strip()
        
        if query.lower() == 'salir':
            print("👋 ¡Hasta la próxima!")
            break
        elif query.lower() == 'historial':
            history_manager.show_history()
        else:
            unified_search(query, local_first=True, top_k=3)
