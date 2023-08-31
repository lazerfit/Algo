d = {}
for _ in range(int(input())):
    x = input()
    if d.get(x):
        d[x] += 1
    else:
        d[x] = 1

sorted_dic = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(sorted_dic[0][0])