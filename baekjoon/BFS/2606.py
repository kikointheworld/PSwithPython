'''
https://www.acmicpc.net/problem/2606
'''
import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

graph = []

ans = [0] * (n+1)

for i in range(n + 1):
    graph.append([])

# 그래프 생성해줌.

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    if ans[x] == 1:
        return
    if ans[x] == 0:
        ans[x] = 1
    for i in graph[x]:
        dfs(i)

dfs(1)

print(sum(ans) - 1)
