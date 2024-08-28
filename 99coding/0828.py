import copy
from collections import deque

def solution(cards):
    cards = [i - 1 for i in cards]
    l = len(cards)
    groups = []
    visited = [0] * l
    for i in range(l):
        if visited[i]:
            continue
        visited[i] = 1
        group = [i]
        next = cards[i]
        while(True):
            if visited[next]:
                break
            visited[next] = 1
            group.append(next)
            next = cards[next]
        groups.append(group)
        
    tmp = [len(i) for i in groups]
    tmp.sort()
    
    if len(tmp) < 2:
        return 0
    else:
        return tmp[-1] * tmp[-2]
     
