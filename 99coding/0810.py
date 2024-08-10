import heapq as hq

def solution(n, costs):
    cnt = 1
    q = []
    visited = [1] + [0] * (n-1)
    ans = 0
    graph = [[] for _ in range(n)]
    for a, b, cost in costs:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    for a, cost in graph[0]:
        hq.heappush(q, (cost, a))
        
    while(q and cnt < n):
        now_cost, dest = hq.heappop(q)
        
        if visited[dest]:
            continue
        else:
            visited[dest] = 1
            cnt += 1
            ans += now_cost
            for a, cost in graph[dest]:
                hq.heappush(q, (cost, a))
            
        
    return ans
