from task_hard_6 import demonstrate_module
from task_hard_8 import binary_search
from task_medium_1 import print_multiplication_table
from task_medium_5 import get_prime_numbers
from task_medium_7 import count_vowels


def main() -> None:
    """Продемонстрировать выполнение заданий лабораторной работы №2."""
    print("Среднее задание №1 — таблица умножения")
    print_multiplication_table()

    print("\nСреднее задание №5 — простые числа до 100")
    print(get_prime_numbers())

    print("\nСреднее задание №7 — подсчёт гласных")
    text = "Методы и технологии программирования"
    print(f"Строка: {text}")
    print(f"Количество гласных: {count_vowels(text)}")

    print("\nПовышенное задание №6 — собственный модуль")
    demonstrate_module()

    print("\nПовышенное задание №8 — бинарный поиск")
    numbers = [2, 5, 8, 11, 15, 21, 34, 55]
    target = 21
    index = binary_search(numbers, target)

    if index != -1:
        print(f"Число {target} найдено. Индекс: {index}")
    else:
        print(f"Число {target} не найдено.")


if __name__ == "__main__":
    main()
