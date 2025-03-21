# 🍽️ Recipe Recommender - AI-powered Recipe Search

Welcome to the **Recipe Recommender**, an AI-powered system for retrieving recipes based on user queries, generating high-quality images of the selected dishes, and translating recipes into multiple languages (English, Portuguese, and Spanish). This project leverages **FAISS** for vector search, **Sentence Transformers** for embeddings, and **Stable Diffusion** for image generation.

---

## 📌 Features
- **Natural language search** for recipes based on ingredient descriptions or dish names.
- **Multilingual support**: English, Portuguese, and Spanish.
- **AI-generated images** of the retrieved recipes using Stable Diffusion (Colab version only).
- **Efficient search** using FAISS and precomputed embeddings.
- **Dataset download automation** via Google Drive.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mikael-vestri/recipe-recommender.git
cd recipe-recommender2
```

### 2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ Download Required Data
Since FAISS index and dataset files are large, they are stored in Google Drive. Run the script below to download them:
```bash
python download_data.py
```

### 4️⃣ Run the Recipe Search
Run the main script to search for recipes:
```bash
python main.py
```
This will prompt you to:
- Select a language.
- Enter a search query (e.g., "chocolate cake").
- Retrieve the best matching recipes and display their details.

---

## 📂 Repository Structure

📁 `recipe-recommender2/`  
├── 📄 `README.md` *(This document)*  
├── 📄 `requirements.txt` *(Dependencies list)*  
├── 📄 `Recipe Recommendation AI Project.pdf` *(Project report & methodology explanation)*  
├── 📄 `download_data.py` *(Script to download required datasets from Google Drive)*  
├── 📁 `src/` *(Main project scripts)*  
│   ├── 📄 `main.py` *(Main script to run the recipe search)*  
│   ├── 📄 `search.py` *(Handles FAISS search and recipe retrieval)*  
│   ├── 📄 `translate.py` *(Handles translation of recipes into multiple languages)*  
│   ├── 📄 `generate_image.py` *(AI-based recipe image generation - Only for Colab)*  
│   ├── 📄 `vectorize.py` *(Script to process and vectorize the dataset)*  
│   ├── 📄 `preprocess.py` *(Dataset cleaning & preparation)*  

---

## 📖 Methodology
For a detailed explanation of the models used (FAISS, Sentence Transformers, Stable Diffusion), see **`Recipe Recommendation AI Project.pdf`**.

---

## 🛠️ Future Improvements
- Improve embedding quality for better search results.
- Enhance image generation with more refined prompts.
- Implement a web interface for a better user experience.

---

## 📜 License
This project is open-source and available under the MIT License.

Happy cooking! 🍕🥗🍰

