n = int(input())
fib = [[] for _ in range(n + 1)]
fib[0] = 0
fib[1] = 1
for i in range(2, n + 1):
    if fib[i - 1] >= 0 and fib[i - 2] >= 0:
        fib[i] = fib[i - 1] + fib[i - 2]

print(fib[n])