import pandas as pd
import ast

def clean_list_column(column):
    """Converts list-like strings to readable strings."""
    if isinstance(column, str):
        try:
            parsed_list = ast.literal_eval(column)
            return ", ".join(parsed_list)
        except (SyntaxError, ValueError):
            return column
    return column

def preprocess_dataset(input_path, output_path):
    df = pd.read_csv(input_path)
    columns_to_keep = ["title", "ingredients", "directions", "NER"]
    df = df[columns_to_keep]

    df["ingredients"] = df["ingredients"].apply(clean_list_column)
    df["directions"] = df["directions"].apply(clean_list_column)
    df["NER"] = df["NER"].apply(clean_list_column)

    df.dropna(subset=["title", "ingredients", "directions", "NER"], inplace=True)

    df["title"] = df["title"].str.lower()
    df["ingredients"] = df["ingredients"].str.lower()
    df["directions"] = df["directions"].str.lower()
    df["NER"] = df["NER"].str.lower()

    df.to_csv(output_path, index=False)
    print(f"✅ Dataset preprocessado e salvo em {output_path}")

if __name__ == "__main__":
    preprocess_dataset("data/full_dataset.csv", "data/processed_dataset.csv")
