class HistoryManager:
    def __init__(self):
        self.history = []

    def add_query(self, query: str):
        self.history.append(query)

    def show_history(self):
        if not self.history:
            print("📂 No hay historial de consultas.")
            return
        print("\n📜 Historial de Consultas:")
        for i, query in enumerate(self.history, 1):
            print(f"{i}. {query}")
