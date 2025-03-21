from search import search_recipe
from translate import translate_recipe
from generate_image import generate_recipe_image

LANG_OPTIONS = {"en": "English", "pt": "Português", "es": "Español"}

def main():
    lang = input("\n🌍 Choose language (en, pt, es): ").strip().lower()
    if lang not in LANG_OPTIONS:
        print("❌ Invalid language. Defaulting to English.")
        lang = "en"

    query = input("\n🔍 Enter dish name or description: ").strip()
    results = search_recipe(query)

    for i, recipe in enumerate(results):
        if lang != "en":
            recipe = translate_recipe(recipe, lang)

        print(f"\n🔹 Recommendation {i+1}")
        print(f"🍽️ {recipe['title']}")
        print(f"🛒 {recipe['ingredients']}")
        print(f"📖 {recipe['directions']}")
        print(f"⚡ Distance: {recipe['distance']}")

        # generate_recipe_image(recipe["title"])

if __name__ == "__main__":
    main()
