import sys

input = sys.stdin.readline

N = int(input())
milk = []
for _ in range(N):
    milk.append(int(input()))

milk.sort(reverse=True)
count = 0
temp = 1
if len(milk) > 3:
    for i in range(len(milk)):
        if temp % 3:
            count += milk[i]
            temp += 1
        else:
            temp = 1
else:
    for i in range(len(milk)):
        count += milk[i]
print(count)