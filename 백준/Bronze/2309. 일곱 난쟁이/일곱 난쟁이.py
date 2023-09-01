from itertools import combinations

v = []
result = []
for _ in range(9):
    v.append(int(input()))

for i in combinations(v, 7):
    if sum(i) == 100:
        result.append(sorted(i))

for j in result[0]:
    print(j)