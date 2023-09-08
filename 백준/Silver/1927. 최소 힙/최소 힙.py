import heapq
import sys

input=sys.stdin.readline
arr = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(arr, x)
    else:
        print(heapq.heappop(arr) if arr else 0)