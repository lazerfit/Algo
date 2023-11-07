import sys

input = sys.stdin.readline

N = int(input())

meet = []
for i in range(N):
    a, b = map(int, input().split())
    meet.append((a, b))

meet.sort(key=lambda x: (x[1], x[0]))

res = end = 0
for s, e in meet:
    if s >= end:
        res += 1
        end = e

print(res)