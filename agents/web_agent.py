import os
import sys
from serpapi import GoogleSearch
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

if not SERPAPI_API_KEY:
    raise ValueError("❌ ERROR: No se encontró la API Key de SerpAPI en el archivo .env")

# Función para realizar una búsqueda en línea con SerpAPI
def search_online(query: str, num_results: int = 5):
    print(f'🌐 Realizando búsqueda en línea para: "{query}"')
    
    search = GoogleSearch({
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    })
    
    results = search.get_dict()
    if "error" in results:
        print(f"⚠️ Error en la búsqueda: {results['error']}")
        return
    
    if "organic_results" not in results:
        print("⚠️ No se encontraron resultados en la web.")
        return

    print("\n🔗 Resultados encontrados en la web:")
    for i, result in enumerate(results["organic_results"][:num_results], start=1):
        print(f"{i}. {result['title']}\n{result['link']}\n")

# Ejemplo de uso
if __name__ == '__main__':
    query = "Últimas noticias sobre inteligencia artificial"
    search_online(query)
