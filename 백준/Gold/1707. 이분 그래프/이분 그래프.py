from collections import deque
import sys

input = sys.stdin.readline

# 이분 그래프 : 인접한 정점끼리 서로 다른 색을 칠해 모든 노드를 두 가지 색으로만 나타낼 수 있는 그래프

def bfs(start):
    dq = deque([start])
    while dq:
        v = dq.popleft()

        for i in graph[v]:
            if not colors[i]:
                dq.append(i)
                colors[i] = -1 * colors[v]
            elif colors[i] == colors[v]:
                return False
    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    colors = [False] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not colors[i]:
            colors[i] = 1
            res = bfs(i)
            if not res:
                break

    print("YES" if res else "NO")