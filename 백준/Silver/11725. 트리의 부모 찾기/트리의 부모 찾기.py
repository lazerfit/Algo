import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dq = deque([1])
res = [0] * (N + 1)


def bfs():
    while dq:
        v = dq.popleft()
        for i in graph[v]:
            if not res[i]:
                res[i] = v
                dq.append(i)

bfs()
for e in res[2:]:
    print(e)