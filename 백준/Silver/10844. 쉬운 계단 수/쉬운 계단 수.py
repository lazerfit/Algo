MOD = 1_000_000_000
n = int(input())

cache = [[0] * 10 for _ in range(101)]
for j in range(1, 10):
    cache[1][j] = 1

for i in range(2, 101):
    for j in range(10):
        if j > 0:
            cache[i][j] += cache[i - 1][j - 1]

        if j < 9:
            cache[i][j] += cache[i - 1][j + 1]

ans = 0
for j in range(10):
    ans += cache[n][j]
    ans %= MOD

print(ans)