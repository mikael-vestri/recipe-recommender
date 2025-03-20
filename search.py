import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

DATASET_PATH = "data/processed_dataset.csv"
FAISS_INDEX_PATH = "data/faiss_index_original.bin"

df = pd.read_csv(DATASET_PATH)
faiss_index = faiss.read_index(FAISS_INDEX_PATH)
model = SentenceTransformer("jonny9f/food_embeddings", device="cpu")

def search_recipe(query, k=3):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = faiss_index.search(query_embedding, k)

    results = []
    for i, idx in enumerate(indices[0]):
        receita = df.iloc[idx]
        results.append({
            "title": receita["title"],
            "ingredients": receita["ingredients"],
            "directions": receita["directions"],
            "distance": distances[0][i]
        })

    return results
