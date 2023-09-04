N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
result = 0

for coin in coins:
    result+=K//coin
    K%=coin

print(result)