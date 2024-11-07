from modules.module1 import TransLate, LangDetect, CodeLang, LanguageList

if __name__ == "__main__":
    text = "Начебто працює"
    print("Переклад:", TransLate(text, 'auto', 'en'))
    print("Визначення мови:", LangDetect(text))
    print("Список мов:", LanguageList("screen", text))
