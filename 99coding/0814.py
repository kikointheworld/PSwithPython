from collections import deque

def solution(n, edge):
    answer = 0
    visited = [1, 1] + [0] * (n-1)
    graph = [[] for _ in range(n + 1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    q = deque()
    q.append((1, 0))
    ans_cnt = 0
    while(q):
        now, cnt = q.popleft()
        for next in graph[now]:
            if visited[next]:
                continue
            visited[next] = 1
            q.append((next, cnt + 1))
            if cnt + 1 > ans_cnt:
                ans_cnt = cnt + 1
                answer = 1
            elif cnt + 1 == ans_cnt:
                answer += 1
            
            
    return answer




