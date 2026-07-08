from deep_translator import GoogleTranslator


def translate_to_english(text):
    """
    Detect the input language automatically
    and translate it to English.
    """
    return GoogleTranslator(
        source="auto",
        target="en"
    ).translate(text)


def translate_from_english(text, target_language):
    """
    Translate English text to the selected language.
    """

    language_map = {
        "English": "en",
        "Hindi": "hi",
        "Marathi": "mr",
        "French": "fr",
        "Spanish": "es"
    }

    # No translation needed
    if target_language == "English":
        return text

    return GoogleTranslator(
        source="en",
        target=language_map[target_language]
    ).translate(text)