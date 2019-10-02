coins = [1, 2, 5, 10, 20, 50, 100, 200]


def count_options(pences, optional_coins):
    options = 0
    for coin in optional_coins:
        if coin == pences:
            options += 1
        if coin < pences:
            options += count_options(pences - coin, [c for c in optional_coins if c <= coin])
    return options


print(count_options(200, coins))
