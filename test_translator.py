from utils.translator import (
    translate_to_english,
    translate_from_english
)

text = "रजेचे धोरण काय आहे?"

english = translate_to_english(text)

print("English:")
print(english)

marathi = translate_from_english(
    "Employees are entitled to Casual Leave and Sick Leave.",
    "Marathi"
)

print("\nMarathi:")
print(marathi)