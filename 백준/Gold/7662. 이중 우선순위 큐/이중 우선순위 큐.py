import sys
from heapq import heappop, heappush

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    min_h, max_h = [], []
    d = {}
    k = int(input())
    for i in range(k):
        c, n = input().split()
        if c == "I":
            heappush(min_h, (int(n), i))
            heappush(max_h, (-int(n), i))
            d[i] = True
        else:
            if int(n) == 1:
                while True:
                    if len(max_h) and not d[max_h[0][1]]:
                        heappop(max_h)
                    else:
                        break
                if len(max_h):
                    mt = heappop(max_h)
                    d[mt[1]] = False
            else:
                while True:
                    if len(min_h) and not d[min_h[0][1]]:
                        heappop(min_h)
                    else:
                        break
                if len(min_h):
                    t = heappop(min_h)
                    d[t[1]] = False

    while True:
        if len(max_h) and not d[max_h[0][1]]:
            heappop(max_h)
        else:
            break
    while True:
        if len(min_h) and not d[min_h[0][1]]:
            heappop(min_h)
        else:
            break

    if not len(max_h):
        print("EMPTY")
    else:
        print(f"{-max_h[0][0]} {min_h[0][0]}")