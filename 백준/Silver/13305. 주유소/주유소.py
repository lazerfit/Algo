import sys

input = sys.stdin.readline

town = []
gas = []
N = int(input())
town = list(map(int, input().split()))
gas = list(map(int, input().split()))

res = 0
i = 0
min_gas = 10001
while i < len(town):
    if gas[i] < min_gas:
        min_gas = gas[i]
    res += min_gas * town[i]
    i += 1

print(res)