# -*- coding: utf-8 -*-
"""
Модуль вычисления максимальной силы драконьей стаи методом
динамического программирования при ограничении на число голов.
"""


def get_max_strength(n: int) -> int:
    """
    Вычисляет максимально возможную силу стаи драконов из N голов.
    Ограничение: особь может иметь от 1 до 7 голов включительно.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        max_val = 0
        limit = min(i, 7)
        for j in range(1, limit + 1):
            product = dp[i - j] * j
            if product > max_val:
                max_val = product
        dp[i] = max_val

    return dp[n]


def main():
    print("=== Расчет максимальной силы драконьей стаи ===")
    try:
        raw_input_data = input("Введите суммарное количество голов N (0 < N < 100): ").strip()
        if not raw_input_data:
            print("Ошибка: введены пустые данные.")
            return

        n = int(raw_input_data)
        if 0 < n < 100:
            result = get_max_strength(n)
            print(f"Максимально возможная сила стаи из {n} голов: {result}")
        else:
            print("Ошибка: Число голов должно находиться в диапазоне от 1 до 99.")
    except ValueError:
        print("Ошибка: Входные данные должны быть корректным целым числом.")


if __name__ == "__main__":
    main()

