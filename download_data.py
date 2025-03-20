import os
import gdown

# Mapping files to download
files = {
    "data/faiss_index.bin": "https://drive.google.com/uc?id=1flF3u7iy4kzi58GBZnNEz5H11A9Rny4h",
    "data/processed_dataset.csv": "https://drive.google.com/uc?id=1eXA_cnZkuQCafWSBI1hh_naPdnXVDC0R"
}

# create "data" folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# download each file
for file_path, url in files.items():
    print(f"📥 Downloading {file_path}...")
    gdown.download(url, file_path, quiet=False)

print("✅ Download finished! You can now run the program normally...")