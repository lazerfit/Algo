from collections import deque

N = int(input())
chk = [0] * (N + 1)


def bfs():
    dq = deque([N])
    while dq:
        v = dq.popleft()
        if v == 1:
            print(chk[v])
        else:
            for i in (
                v // 3 if v % 3 == 0 else 0,
                v // 2 if v % 2 == 0 else 0,
                v - 1 if v - 1 > 0 else 0,
            ):
                if i > 0 and chk[i] == 0:
                    chk[i] = chk[v] + 1
                    dq.append(i)


bfs()