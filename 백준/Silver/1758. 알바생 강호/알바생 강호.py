import sys

input = sys.stdin.readline

tip = []
for _ in range(int(input())):
    tip.append(int(input()))

tip.sort(reverse=True)
count = 0
for i in range(len(tip)):
    temp = tip[i] - ((i + 1) - 1)
    if temp >= 0:
        count += temp
    else:
        continue

print(count)