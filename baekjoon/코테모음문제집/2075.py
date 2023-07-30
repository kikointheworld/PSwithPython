import heapq

n = int(input())

q = []

for _ in range(n):
    for i in list(map(int, input().split())):
        if len(q) >= n:
            heapq.heappushpop(q, i)
        else:
            heapq.heappush(q, i)
print(heapq.heappop(q))
    


