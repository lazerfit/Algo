import sys

input = sys.stdin.readline

n_a, n_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

common = len(a & b)
print((n_a - common) + (n_b - common))
