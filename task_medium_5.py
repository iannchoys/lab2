def is_prime(number: int) -> bool:
    """Проверить, является ли число простым."""
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def get_prime_numbers(limit: int = 100) -> list[int]:
    """Вернуть список простых чисел от 2 до limit включительно."""
    primes = []

    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)

    return primes


if __name__ == "__main__":
    print(get_prime_numbers())
