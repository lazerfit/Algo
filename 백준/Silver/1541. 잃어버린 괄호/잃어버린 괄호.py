n = input().split("-")
res = 0
for i in n[0].split("+"):
    res += int(i)

for i in n[1:]:
    minus = i.split("+")
    for j in minus:
        res -= int(j)

print(res)