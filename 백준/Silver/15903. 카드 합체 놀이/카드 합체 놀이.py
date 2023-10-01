import heapq

n, m = map(int, input().split())

cards = list(map(int, input().split()))
heapq.heapify(cards)

for i in range(m):
    prev = heapq.heappop(cards)
    curr = heapq.heappop(cards)
    s = prev + curr
    heapq.heappush(cards, s)
    heapq.heappush(cards, s)

print(sum(cards))