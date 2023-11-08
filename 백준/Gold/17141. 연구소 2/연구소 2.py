from collections import deque
from itertools import combinations

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dq = deque()
dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def is_validate(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(v):
    dq = deque(v)
    visited = [[-1] * N for _ in range(N)]
    m = 0
    for x, y in v:
        visited[x][y] = 0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_validate(nx, ny) and visited[nx][ny] == -1 and board[nx][ny] != 1:
                dq.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                m = max(m, visited[x][y] + 1)
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and board[i][j] != 1:
                return float("inf")
    return m


bomb = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            bomb.append((i, j))


res = float("inf")
for v in combinations(bomb, M):
    res = min(res, bfs(v))

if res == float("inf"):
    print(-1)
else:
    print(res)
