import heapq
import sys


arr = []

input = sys.stdin.readline
for _ in range(int(input())):
    num = int(input())
    if num:
        heapq.heappush(arr, (abs(num), num))
    else:
        print(heapq.heappop(arr)[1] if arr else 0)