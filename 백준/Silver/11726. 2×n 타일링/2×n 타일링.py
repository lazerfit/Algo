n = int(input())
fib = [0] * 1001
fib[1] = 1
fib[2] = 2

for i in range(3, 1001):
    if fib[i] == 0:
        fib[i] = fib[i - 1] + fib[i - 2]

print(fib[n] % 10007)