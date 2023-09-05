from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

v = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for i in range(M):
    v1, v2 = map(int, input().split())
    v[v1].append(v2)
    v[v2].append(v1)


def dsf(start):
    visited[start] = True
    s = v[start]
    for elem in s:
        if not visited[elem]:
            dsf(elem)


count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dsf(i)
        count += 1

print(count)
