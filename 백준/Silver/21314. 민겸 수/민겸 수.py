m = input()
res_min = []
res_max = []

for i in m.split("K"):
    if i:
        res_min.append(str(10 ** (len(i) - 1)))
        res_max.append(str(5 * (10 ** len(i))))
    else:
        res_min.append("")
        res_max.append("5")

print("".join(res_max[:-1]) + "1" * (len(res_max[-1]) - 1))
print("5".join(res_min))
