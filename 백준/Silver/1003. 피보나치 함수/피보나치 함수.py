for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print("1 0")
    else:
        fib = [[] for _ in range(n + 1)]
        fib[0] = (1, 0)
        fib[1] = (0, 1)
        for i in range(2, n + 1):
            if (
                fib[i - 1][0] >= 0
                and fib[i - 2][0] >= 0
                and fib[i - 1][1] >= 0
                and fib[i - 2][1] >= 0
            ):
                fib[i] = (fib[i - 1][0] + fib[i - 2][0], fib[i - 1][1] + fib[i - 2][1])

        print(*fib[n])