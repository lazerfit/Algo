from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dq = deque()
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    edges[v1].append(v2)
    edges[v2].append(v1)

visited = [False for _ in range(N + 1)]


def bfs(start):
    dq.append(start)
    visited[start] = True
    while dq:
        vertex = dq.popleft()
        for val in edges[vertex]:
            if not visited[val]:
                visited[val] = True
                dq.append(val)


count = 0
for k in range(1, N + 1):
    if not visited[k]:
        bfs(k)
        count += 1

print(count)