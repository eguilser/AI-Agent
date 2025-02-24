# 🤖 **IA-Agent: An Intelligent Agent for File and Web Searches**

IA-Agent is a powerful AI-driven project designed to perform advanced searches both in local files and on the web. It leverages Pinecone for vector search, SerpAPI for online queries, and Hugging Face's language models for natural language processing. The project includes a query history feature and a caching system to boost efficiency.

---

## 🚀 **Key Features**

- **File Search:** Uses Pinecone to index and search through local documents.
- **Web Search:** Integrates with SerpAPI to fetch the most relevant web results.
- **Query History:** Keeps a record of past searches for easy reference.
- **Caching System:** Speeds up responses for repeated queries.
- **Unified Search:** Combines file and web search in a single query.

---

## 🧰 **Technologies Used**

- **Python 3.10+**
- **Pinecone:** Vector database for efficient search.
- **SerpAPI:** Real-time search engine results.
- **Hugging Face:** Advanced NLP with language models.
- **Langchain:** For managing prompts and interactions.

---

## 📂 **Project Structure**

```plaintext
IA-Agent/
├─ agents/
│   ├─ file_agent.py
│   ├─ web_agent.py
│   ├─ unified_agent.py
│   ├─ history_manager.py
│   └─ cache_manager.py
├─ config/
│   ├─ config.py
│   └─ upload_data.py
├─ data/
│   └─ data.txt
├─ embeddings/
│   └─ huggingface_embeddings.py
├─ env/
├─ .env
├─ .gitignore
├─ requirements.txt
└─ README.md
```

---

## ⚙️ **Setup & Installation**

### 1. **Clone the Repository:**

```bash
git clone https://github.com/your_username/IA-Agent.git
cd IA-Agent
```

### 2. **Set Up Virtual Environment:**

```bash
python -m venv env
source env/bin/activate        # On Linux/Mac
env\Scripts\activate         # On Windows
```

### 3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

### 4. **Configure Environment Variables:**
Create a `.env` file with the following content:

```plaintext
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_env
HUGGINGFACE_API_KEY=your_huggingface_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

### 5. **Load Data into Pinecone:**

```bash
python config/upload_data.py
```

---

## 🚦 **How to Use**

### Run the Unified Agent

```bash
python agents/unified_agent.py
```

### Available Commands

- **Run a search:** Type your query directly.
- **View history:** Type `history`.
- **Exit the program:** Type `exit`.

---

## 🌐 **Screenshots**

### 1. **File Search Example:**

![AgenteIAfile](https://github.com/user-attachments/assets/8792489c-7c6d-4cde-b142-587f0d846dd5)

### 2. **Web Search Example:**
![AgenteIAweb](https://github.com/user-attachments/assets/33c008f7-d7bf-48ed-8eab-fa6255913859)


### 3. **Unified Search Results:**
![AgenteIA1](https://github.com/user-attachments/assets/a026bff8-f11a-4eed-a8cd-d0e97d267038)


---

## 🧠 **Advanced Tips**

- **Update Dependencies:**
```bash
pip install --upgrade -r requirements.txt
```

- **Clear Cache:**
```bash
python -c 'from agents.cache_manager import clear_cache; clear_cache()'
```

---

## 📄 **License**

This project is licensed under the MIT License.

---

## 🤝 **Contributing**

1. **Fork the repository**
2. **Create a new branch:** `git checkout -b feature/YourFeature`
3. **Commit your changes:** `git commit -m 'Add YourFeature'`
4. **Push to the branch:** `git push origin feature/YourFeature`
5. **Open a Pull Request**

---

## 💬 **Support**

For any issues, please open an **issue** or reach out via [email@domain.com](mailto:email@domain.com).

