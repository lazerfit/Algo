import sys
sys.setrecursionlimit(10**6)

n, r = map(int, input().split())
board = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    board[i][0] = 1
    board[i][i] = 1


def f(n, r):
    if board[n][r] == 0:
        board[n][r] = f(n - 1, r - 1) + f(n - 1, r)
    return board[n][r] % 10007


print(f(n, r))