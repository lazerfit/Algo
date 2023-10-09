n = int(input())
t1, t2 = map(int, input().split())
m = int(input())
board = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

stack = [t1]

count = -1
while stack:
    x = stack.pop()
    for elem in board[x]:
        if elem == t2:
            count = visit[x] + 1
            break
        if not visit[elem]:
            stack.append(elem)
            visit[elem] = visit[x] + 1

print(count)