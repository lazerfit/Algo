from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

chk = [[False] * m for _ in range(n)]
res = [[-1] * m for _ in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def is_validate(x, y):
    return 0 <= x < n and 0 <= y < m and not chk[x][y]


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            target = (i, j)
            res[i][j] = 0
        if not graph[i][j]:
            res[i][j] = 0


def bfs(start_x, start_y):
    dq = deque([(start_x, start_y)])
    chk[start_x][start_y] = True
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_validate(nx, ny) and graph[nx][ny] == 1:
                dq.append((nx, ny))
                chk[nx][ny] = True
                res[nx][ny] = res[x][y] + 1


bfs(target[0], target[1])
for i in range(n):
    for j in range(m):
        print(res[i][j], end=" ")
    print()
