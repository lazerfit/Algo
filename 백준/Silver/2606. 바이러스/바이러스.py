from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(int(input())):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def bfs():
    dq = deque([1])
    visited = [False] * (N + 1)
    visited[1] = True
    result = 0
    while dq:
        v = dq.popleft()
        for elem in graph[v]:
            if not visited[elem]:
                visited[elem] = True
                dq.append(elem)
                result += 1
    return result


print(bfs())
