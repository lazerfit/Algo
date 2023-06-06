a = list(input())
converted_a = []
alphabets = []

for i in a:
    converted_a.append(ord(i) - 96)

for i in range(1, 27):
    alphabets.append(i)

for alphabet in alphabets:
    if alphabet in converted_a:
        print(converted_a.index(alphabet), end=" ")
    else:
        print(-1, end=" ")