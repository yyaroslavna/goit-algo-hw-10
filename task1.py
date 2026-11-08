coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount = amount % coin

    return result


def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    previous = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                previous[i] = coin

    result = {}
    current = amount

    while current > 0:
        coin = previous[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Динамічне програмування:", find_min_coins(amount))
