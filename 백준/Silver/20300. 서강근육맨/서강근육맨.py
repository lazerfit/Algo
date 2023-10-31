N = int(input())
m = list(map(int, input().split()))
m.sort()
res = 0

if len(m) % 2 == 0:
    for i in range(len(m) // 2):
        res = max(res, m[i] + m[-1 - i])
else:
    for i in range(len(m) // 2):
        res = max(res, m[i] + m[-2 - i])
    res = max(res, m[-1])

print(res)