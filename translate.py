from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    return GoogleTranslator(source="en", target=target_lang).translate(text)

def translate_recipe(recipe, target_lang):
    return {
        "title": translate_text(recipe["title"], target_lang),
        "ingredients": translate_text(recipe["ingredients"], target_lang),
        "directions": translate_text(recipe["directions"], target_lang),
        "distance": recipe["distance"]
    }
