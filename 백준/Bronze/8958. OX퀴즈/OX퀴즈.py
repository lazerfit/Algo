r = int(input())

for _ in range(r):
    s = list(input())
    for i in range(len(s)):
        if s[i] == "O":
            s[i] = 1
        else:
            s[i] = 0
    for i in range(1, len(s)):
        if s[i - 1] >= 1 & s[i] != 0:
            s[i] = s[i - 1] + 1
    print(sum(s))