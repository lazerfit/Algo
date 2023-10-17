import sys

input = sys.stdin.readline

N = int(input())
energy = list(map(int, input().split()))

energy.sort()

max_v = energy[-1]
for i in range(len(energy) - 1):
    v = energy[i] / 2
    max_v += v

print(max_v)