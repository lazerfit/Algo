from collections import deque

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def is_valid(x, y):
    return 0 <= x < R and 0 <= y < C


meet = False


def bfs(x, y, graph):
    global meet
    if graph[x][y] == "W":
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid(nx, ny) and graph[nx][ny] == "S":
                meet = True
                break
    elif graph[x][y] == ".":
        graph[x][y] = "D"


for i in range(R):
    for j in range(C):
        bfs(i, j, graph)

if meet:
    print(0)
else:
    print(1)
    for k in graph:
        print("".join(k))