import sys
import heapq as hq

def input():
    return sys.stdin.readline().rstrip()

heap = []

n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(-1 * hq.heappop(heap))
        else:
            print(0)
    else:
        hq.heappush(heap, -1 * x)
