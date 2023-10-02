import heapq

N = int(input())
graph = []
for _ in range(N):
    for elem in list(map(int, input().split())):
        heapq.heappush(graph, elem)
    if len(graph) > N:
        while len(graph) > N:
            heapq.heappop(graph)

print(graph[0])