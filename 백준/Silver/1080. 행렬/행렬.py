N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]


def rev(a, b):
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            A[i][j] = 1 - A[i][j]


count = 0
if (N < 3 or M < 3) and A != B:
    print(-1)

else:
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                rev(i, j)
                count += 1

    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                count = -1
                break

    print(count)
