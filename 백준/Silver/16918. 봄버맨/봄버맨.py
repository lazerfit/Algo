import sys

input = sys.stdin.readline

R, C, N = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
time = [[0] * C for _ in range(R)]
di = (-1, 0, 1, 0)
dj = (0, -1, 0, 1)


def is_validate(nx, ny):
    return 0 <= nx < R and 0 <= ny < C


def printGraph(graph):
    for i in range(R):
        print("".join(graph[i]))


def bomb1(graph):
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "O":
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if is_validate(ni, nj) and graph[ni][nj] != "O":
                        graph[ni][nj] = "X"
                graph[i][j] = "X"
    for a in range(R):
        for b in range(C):
            if graph[a][b] == "X":
                graph[a][b] = "."
            else:
                graph[a][b] = "O"

    return graph


if N == 1:
    printGraph(graph)
else:
    if not N % 2:
        for i in range(R):
            for j in range(C):
                if graph[i][j] != "O":
                    graph[i][j] = "O"
        printGraph(graph)

    elif N > 1 and N % 4 == 3:
        printGraph(bomb1(graph))

    elif N > 1 and N % 4 == 1:
        graph2 = bomb1(graph)
        printGraph(bomb1(graph2))