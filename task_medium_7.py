VOWELS = "аеёиоуыэюяaeiou"


def count_vowels(text: str) -> int:
    """Подсчитать количество русских и английских гласных в строке."""
    count = 0

    for character in text.lower():
        if character in VOWELS:
            count += 1

    return count


if __name__ == "__main__":
    example_text = "Методы и технологии программирования"
    print(f"Строка: {example_text}")
    print(f"Количество гласных: {count_vowels(example_text)}")
