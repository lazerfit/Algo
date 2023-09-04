N, L = map(int, input().split())
water = list(map(int, input().split()))
count = 1
water.sort()
temp = water[0] - 0.5 + L
for i in range(len(water)):
    if temp < water[i] + 0.5:
        count += 1
        temp = water[i] - 0.5 + L

print(count)