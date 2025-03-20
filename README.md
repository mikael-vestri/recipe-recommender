# 🍽️ Recipe Recommender - AI-powered Recipe Search

Welcome to the **Recipe Recommender**, an AI-powered system for retrieving recipes based on user queries, generating high-quality images of the selected dishes, and translating recipes into multiple languages (English, Portuguese, and Spanish). This project leverages **FAISS** for vector search, **Sentence Transformers** for embeddings, and **Stable Diffusion** for image generation.

---

## 📌 Features
- **Natural language search** for recipes based on ingredient descriptions or dish names.
- **Multilingual support**: English, Portuguese, and Spanish.
- **AI-generated images** of the retrieved recipes using Stable Diffusion.
- **Efficient search** using FAISS and precomputed embeddings.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mikael-vestri/recipe-recommender.git
cd recipe-recommender
```

### 2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Recipe Search
Run the main script to search for recipes:
```bash
python src/main.py
```
This will prompt you to:
- Select a language.
- Enter a search query (e.g., "chocolate cake").
- Retrieve the best matching recipes and display their details.
- Generate an AI-rendered image of the selected recipe.

---

## 📂 Repository Structure

📁 `recipe-recommender/`  
├── 📄 `README.md` *(This document)*  
├── 📄 `requirements.txt` *(Dependencies list)*  
├── 📄 `documentation.pdf` *(Project report & methodology explanation)*  
├── 📁 `src/` *(Main project scripts)*  
│   ├── 📄 `main.py` *(Main script to run the recipe search & image generation)*  
│   ├── 📄 `image_generation.py` *(Stable Diffusion-based image generation)*  
│   ├── 📄 `utils.py` *(Utility functions)*  
├── 📁 `data_processing/` *(Optional: Scripts for dataset processing & FAISS index creation)*  
│   ├── 📄 `vectorize_dataset.py` *(Precomputes embeddings & builds FAISS index)*  
│   ├── 📄 `preprocess_data.py` *(Dataset cleaning & preparation)*  
├── 📁 `examples/` *(Example queries & generated images)*  
│   ├── 📄 `query_example_1.json` *(Example FAISS output)*  
│   ├── 🖼️ `screenshot_1.png` *(Screenshot of the app in action)*  

---

## 📖 Methodology
For a detailed explanation of the models used (FAISS, Sentence Transformers, Stable Diffusion), see **`documentation.pdf`**.

---

## 🛠️ Future Improvements
- Improve embedding quality for better search results.
- Enhance image generation with more refined prompts.
- Implement a web interface for a better user experience.

---

## 📜 License
This project is open-source and available under the MIT License.

Happy cooking! 🍕🥗🍰

