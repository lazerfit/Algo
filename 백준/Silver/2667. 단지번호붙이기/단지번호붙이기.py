from collections import deque

N = int(input())

board = [input() for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

res = []


def bfs(board, start_x, start_y, visited):
    if board[start_x][start_y] == "0":
        return -1
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    count = 1
    while q:
        x, y = q.popleft()
        if board[x][y] == "0":
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[nx][ny] == "1":
                    q.append((nx, ny))
                    count += 1
                visited[nx][ny] = True
    res.append(count)


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(board, i, j, visited)

print(len(res))
for e in sorted(res):
    print(e)