def print_multiplication_table(size: int = 10) -> None:
    """Вывести таблицу умножения от 1 до size."""
    if size <= 0:
        raise ValueError("Размер таблицы должен быть положительным.")

    for row in range(1, size + 1):
        for column in range(1, size + 1):
            print(f"{row * column:4}", end="")
        print()


if __name__ == "__main__":
    print_multiplication_table()
