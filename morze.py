# Словарь для перевода русских букв в азбуку Морзе
morse_code = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
    'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
    'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
    'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
    'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----',
    'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
    'Ю': '..--', 'Я': '.-.-', ' ': ' ',  # Пробел
}

# Обратный словарь для перевода азбуки Морзе в русские буквы
reverse_morse_code = {value: key for key, value in morse_code.items()}

def text_to_morse(text):
    """
    Переводит текст на русском языке в азбуку Морзе.
    """
    morse = []
    for char in text.upper():
        if char in morse_code:
            morse.append(morse_code[char])
        else:
            morse.append('')  # Игнорируем символы, которых нет в словаре
    return ' '.join(morse)

def morse_to_text(morse):
    """
    Переводит азбуку Морзе в текст на русском языке.
    """
    text = []
    for code in morse.split(' '):
        if code in reverse_morse_code:
            text.append(reverse_morse_code[code])
        else:
            text.append('')  # Игнорируем коды, которых нет в словаре
    return ''.join(text)

# Пример использования
if __name__ == "__main__":
    print("Выберите режим:")
    print("1. Русский текст в азбуку Морзе")
    print("2. Азбука Морзе в русский текст")
    choice = input("Введите 1 или 2: ")

    if choice == '1':
        text = input("Введите текст на русском языке: ")
        morse = text_to_morse(text)
        print(f"Азбука Морзе: {morse}")
    elif choice == '2':
        morse = input("Введите азбуку Морзе (разделяйте символы пробелами): ")
        text = morse_to_text(morse)
        print(f"Текст на русском: {text}")
    else:
        print("Некорректный выбор.")
