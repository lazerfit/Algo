N = int(input())
atm = list(map(int, input().split()))
atm.sort()

i = 1
count = 0
while i <= N:
    for j in range(i):
        count += atm[j]
    i += 1

print(count)