a = int(input())
for _ in range(a):
    r, s = input().split()
    result = ""
    for j in s:
        result += int(r) * j
    print(result)