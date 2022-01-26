'''
https://www.acmicpc.net/problem/1260
'''
from collections import deque
import sys

n, m, v = map(int,sys.stdin.readline().split())

graph = []

graph.append([]) # 처음 인덱스는 무시할 것임.

for _ in range(n):
    graph.append([])

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

# DFS

dfs_list = [0] * (n + 1)

def dfs(v):
    if dfs_list[v] == 1:
        return
    dfs_list[v] = 1
    print(v, end = " ")
    for i in graph[v]:
        if dfs_list[i] == 0:
            dfs(i)
    
# BFS

bfs_list = [0] * (n + 1)
def bfs(v):
    bfs_q = deque([v])
    bfs_list[v] = 1
    while bfs_q:
        tmp = bfs_q.popleft()
        print(tmp, end = " ")
        for i in graph[tmp]:
            if bfs_list[i] == 0:
                bfs_q.append(i)
                bfs_list[i] = 1



dfs(v)
print()
bfs(v)
