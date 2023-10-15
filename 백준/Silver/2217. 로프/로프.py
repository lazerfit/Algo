import sys

input = sys.stdin.readline

N = int(input())
rope = []
res = []
for _ in range(N):
    rope.append(int(input()))

rope = sorted(rope)
i = N
for j in range(N):
    res.append(rope[j] * i)
    i -= 1

print(max(res))