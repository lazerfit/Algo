import heapq

N = int(input())
vote = []
cand = []
for _ in range(N):
    vote.append(int(input()))

for elem in vote[1:]:
    heapq.heappush(cand, -elem)


if N == 1:
    count = 0
else:
    count = 0
    while vote[0] <= -cand[0]:
        vote[0] += 1
        temp = heapq.heappop(cand)
        heapq.heappush(cand, temp + 1)
        count += 1

print(count)