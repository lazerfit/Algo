r = int(input())
for _ in range(r):
    h, w, n = map(int, input().split())
    nw = (n // h) + 1
    nh = n % h
    if nh == 0:
        nh = h
        nw = n // h
    print(f"{nh*100+nw}")