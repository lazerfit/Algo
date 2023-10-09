from collections import deque

dx = (-1, 1, 0, 0, 1, 1, -1, -1)
dy = (0, 0, -1, 1, 1, -1, -1, 1)


def is_validate(x, y):
    return 0 <= x < h and 0 <= y < w and not visit[x][y]


def bfs(start_x, start_y, board, visit):
    global count
    if not board[start_x][start_y]:
        return
    elif board[start_x][start_y] and not visit[start_x][start_y]:
        dq = deque([(start_x, start_y)])
        visit[start_x][start_y] = True
        while dq:
            x, y = dq.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if is_validate(nx, ny) and board[nx][ny]:
                    dq.append((nx, ny))
                    visit[nx][ny] = True
        count += 1


while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    else:
        board = [list(map(int, input().split())) for _ in range(h)]
        visit = [[False] * w for _ in range(h)]
        count = 0
        for i in range(h):
            for j in range(w):
                bfs(i, j, board, visit)
        print(count)