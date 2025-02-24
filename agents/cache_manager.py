class CacheManager:
    def __init__(self):
        self.cache = {}

    def add_to_cache(self, query: str, result: str):
        self.cache[query] = result

    def get_from_cache(self, query: str):
        return self.cache.get(query, None)
