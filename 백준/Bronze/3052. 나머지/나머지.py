data = []
result = []
for i in range(10):
    data.append(int(input()))

for i in range(10):
    result.append(data[i] % 42)
print(len(set(result)))