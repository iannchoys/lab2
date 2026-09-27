def binary_search(numbers: list[int], target: int) -> int:
    """Вернуть индекс target в отсортированном списке или -1."""
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = numbers[middle]

        if middle_value == target:
            return middle

        if middle_value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


if __name__ == "__main__":
    sorted_numbers = [2, 5, 8, 11, 15, 21, 34, 55]
    search_target = 21

    index = binary_search(sorted_numbers, search_target)

    if index != -1:
        print(f"Число {search_target} найдено. Индекс: {index}")
    else:
        print(f"Число {search_target} не найдено.")
