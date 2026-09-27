from arithmetic_utils import cube, square


def demonstrate_module() -> None:
    """Продемонстрировать импорт функций из собственного модуля."""
    number = 5

    print(f"Число: {number}")
    print(f"Квадрат: {square(number)}")
    print(f"Куб: {cube(number)}")


if __name__ == "__main__":
    demonstrate_module()