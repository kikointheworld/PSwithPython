from itertools import combinations
from collections import deque
def is_one(a, b):
    l = len(a)
    tmp = 0
    for i in range(l):
        if a[i] != b[i]:
            tmp += 1  
        if tmp > 1:
            return False
    return True
        

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = {k : 0 for k in words + [begin]}
    graph = {k : [] for k in words + [begin]}
    graph[begin] = []
    
    
    for a, b in combinations(words + [begin], 2):
        if is_one(a, b):
            graph[a].append(b)
            graph[b].append(a)
    q = deque()
    q.append((begin, 0))
    visited[begin] = 1
    while(q):
        now, cnt = q.popleft()
        if now == target:
            answer = cnt
            break
        for new in graph[now]:
            if visited[new]:
                continue
            q.append((new, cnt + 1))
            visited[new] = 1
        
    
    return answer
