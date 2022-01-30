'''
https://www.acmicpc.net/problem/2206
'''
import sys
from collections import deque
import copy
isFinish = False


def bfs():
    graph[0][0][0] = 1
    q = deque([[0, 0, 0]])
    while q:
        tmp = q.popleft()
        tmp_x, tmp_y, tmp_z = tmp[0], tmp[1], tmp[2]
        
        if tmp_x == m - 1 and tmp_y == n - 1: # 어쨌든 최종 지점에 도달함.
            global isFinish
            isFinish = True
            return
        
        for i in range(4):
            now_x = tmp_x + dx[i]
            now_y = tmp_y + dy[i]
            now_z = tmp_z
            if now_x == 0 and now_y == 0 : # 시작 지점 벽 뚫기 방지
                continue
            
            if 0 <= now_x < m and 0 <= now_y < n:
                if graph[now_z][now_y][now_x] == 1:
                    if now_z == 0: # 벽 부수기
                        if graph[1][now_y][now_x] != graph[0][now_y][now_x]:
                            continue
                        now_z = 1
                        graph[now_z][now_y][now_x] = graph[tmp_z][tmp_y][tmp_x] + 1
                        q.append([now_x, now_y, now_z]) # 벽 부수고 올라온 상태
                        
                elif graph[now_z][now_y][now_x] == 0 :
                    graph[now_z][now_y][now_x] = graph[tmp_z][tmp_y][tmp_x] + 1
                    q.append([now_x, now_y, now_z])
 

n, m = map(int,sys.stdin.readline().split())

graph = []
tmp1 = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
    

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip()))
    tmp1.append(tmp)
tmp2 = copy.deepcopy(tmp1)
graph.append(tmp1)
graph.append(tmp2)
bfs()
if n == 1 and m == 1:
    print(1)
elif isFinish == False:
    print(-1)
else:
    print(max(graph[0][n-1][m-1], graph[1][n-1][m-1]))
