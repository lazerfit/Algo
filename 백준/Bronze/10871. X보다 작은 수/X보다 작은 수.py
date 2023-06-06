n, x = input().split()
data = list(map(int, input().split()))
for n in data:
    if n < int(x):
        print(n, end=" ")