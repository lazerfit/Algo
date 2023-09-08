import sys

sys.setrecursionlimit(10**6)

n, r = map(int, input().split())
cache = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(r + 1):
        if j == 0 or i == j:
            cache[i][j] = 1
        else:
            cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]

print(cache[n][r] % 10007)