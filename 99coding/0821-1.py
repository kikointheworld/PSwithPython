from collections import deque

def solution(n, computers):
    visited = [0] * n
    ans = 0
    for now in range(n):
        if visited[now]:
            continue
        ans += 1
        q = deque()
        for next in range(n):
            if next != now and not visited[next] and computers[now][next]:
                q.append(next)
                visited[next] = 1
        
        while(q):
            new = q.popleft()
            for new_next in range(n):
                if new_next != new and not visited[new_next] and computers[new][new_next]:
                    q.append(new_next)
                    visited[new_next] = 1
            
        
    return ans
