from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    e1, e2 = map(int, input().split())
    graph[e1][e2] = graph[e2][e1] = 1

result_dfs = []


def dfs(start):
    result_dfs.append(start)
    visited[start] = 1
    for i in range(1, N + 1):
        if graph[start][i] and not visited[i]:
            dfs(i)
    return result_dfs


def bfs(start):
    dq = deque()
    result_bfs = []
    dq.append(start)
    result_bfs.append(start)
    visited = [0] * (N + 1)
    visited[start] = 1
    while dq:
        v = dq.popleft()
        for i in range(1, N + 1):
            if graph[v][i] and not visited[i]:
                dq.append(i)
                visited[i] = 1
                result_bfs.append(i)

    return result_bfs

print(*dfs(V))
print(*bfs(V))