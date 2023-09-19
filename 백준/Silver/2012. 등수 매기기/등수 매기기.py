import sys

input = sys.stdin.readline
N = int(input())

s = sorted([int(input()) for _ in range(N)])

res = 0
for i in range(len(s)):
    if s[i] != i + 1:
        res += abs((i + 1) - s[i])

print(res)