import sys

input = sys.stdin.readline

town = []
gas = []
N = int(input())
town = list(map(int, input().split()))
gas = list(map(int, input().split()))

res = 0
min_gas = gas.index(min(gas[:-2]))

if not min_gas:
    for i in range(len(town)):
        res += town[i] * gas[min_gas]
else:
    for i in range(min_gas):
        res += town[i] * gas[i]
    for j in range(min_gas, len(town)):
        res += town[i] * gas[min_gas]
print(res)