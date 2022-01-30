'''
https://www.acmicpc.net/problem/1707
'''
import sys
sys.setrecursionlimit(100000) # 재귀를 돌릴 경우에는 무조건 넣어주자.....
# blue 1, red 2...로 이분 그래프 나누기

def dfs(start, change):
    global isYes
    # 선이 겹치면 그냥 종료
    if isYes == 0:
        return

    # 선을 방문한 적이 있다면...
    if isVisited[start]:
        if isVisited[start] != change:
            isYes = 0
            return 
        else:
            return

    isVisited[start] = change

    change = 2 if change == 1 else 1
    
    for i in graph[start]:
        if isVisited[i]:
            if isVisited[i] != change:
                isYes = 0
                return
            else:
                continue
        dfs(i, change)




k = int(sys.stdin.readline())

for _ in range(k):
    u, v = map(int,sys.stdin.readline().split())
    # value = [0] * (u + 1)
    isVisited = [0] * (u + 1)
    
    # 그래프 초기화 완료
    graph =[]
    for _ in range(u + 1):
        graph.append([])
    for _ in range(v):
        a, b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    isYes = 1
    
    for i in range(u + 1):
        if not isVisited[i]:
            dfs(i, 1)

    
    if isYes:
        print("YES")
    else:
        print("NO")
