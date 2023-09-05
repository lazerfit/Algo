from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
dq = deque()
for _ in range(M):
    temp = tuple(map(int, input().split()))
    edges.append(temp)

adj = {}
for i in range(1, N + 1):
    adj[i] = []

for edge in edges:
    vertex1 = edge[0]
    vertex2 = edge[1]
    adj[vertex1].append(vertex2)
    adj[vertex2].append(vertex1)

visited = {i: False for i in range(1, N + 1)}


def bfs(start):
    dq.append(start)
    result = []
    visited[start] = True
    while dq:
        vertex = dq.popleft()
        result.append(vertex)
        for val in adj[vertex]:
            if visited[val] == False:
                visited[val] = True
                dq.append(val)


count = 0
for k in range(1, N + 1):
    if not visited[k]:
        bfs(k)
        count += 1

print(count)