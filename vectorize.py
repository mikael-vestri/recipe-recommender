import pandas as pd
import numpy as np
import faiss
import os
from sentence_transformers import SentenceTransformer

DATASET_PATH = "data/processed_dataset.csv"
SAVE_DIR = "data/embeddings_batches/"
FAISS_INDEX_PATH = "data/faiss_index_original.bin"

def create_text_representation(row):
    return f"Recipe name: {row['title']}. Main Ingredients: {row['ingredients']}. Cooking Instructions: {row['directions']}."

def vectorize_dataset():
    df = pd.read_csv(DATASET_PATH)
    text_data = df.apply(create_text_representation, axis=1).tolist()

    model = SentenceTransformer("jonny9f/food_embeddings", device="cuda")

    os.makedirs(SAVE_DIR, exist_ok=True)
    
    batch_size = 25000
    existing_batches = {int(f.split('_')[-1].split('.')[0]) for f in os.listdir(SAVE_DIR) if f.startswith("embeddings_batch_")}

    for i in range(0, len(text_data), batch_size):
        batch_num = i // batch_size
        batch_filename = f"{SAVE_DIR}embeddings_batch_{batch_num}.npy"

        if batch_num in existing_batches:
            print(f"⚡ Batch {batch_num} already exist. Skipping...")
            continue

        batch_texts = text_data[i:i + batch_size]
        batch_embeddings = model.encode(batch_texts, batch_size=32, convert_to_numpy=True)
        np.save(batch_filename, batch_embeddings)
        print(f"✅ Batch {batch_num} saved at {batch_filename}")

    embeddings_list = [np.load(os.path.join(SAVE_DIR, batch)) for batch in sorted(os.listdir(SAVE_DIR))]
    embeddings = np.vstack(embeddings_list)

    dimension = embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(embeddings)

    faiss.write_index(faiss_index, FAISS_INDEX_PATH)
    print(f"✅ FAISS index saved at {FAISS_INDEX_PATH}")

if __name__ == "__main__":
    vectorize_dataset()
