import sys

input = sys.stdin.readline
N, P = map(int, input().split())

melody = [[] for _ in range(7)]

count = 0
for _ in range(N):
    n, p = map(int, input().split())

    if not melody[n]:
        melody[n].append(p)
        count += 1
    else:
        while True:
            if not melody[n]:
                melody[n].append(p)
                count += 1
                break
            if melody[n][-1] == p:
                break
            if melody[n][-1] < p:
                melody[n].append(p)
                count += 1
            else:
                melody[n].pop()
                count += 1

print(count)