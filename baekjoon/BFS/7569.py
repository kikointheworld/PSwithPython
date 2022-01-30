'''
https://www.acmicpc.net/problem/7569
'''
from collections import deque
import sys

m, n, h = map(int,sys.stdin.readline().split())

tomato = []

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0 ,0]
dz = [0, 0, 0, 0, 1, -1]


for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append( list(map(int,sys.stdin.readline().split())))
    tomato.append(tmp)


q = deque()

# print(tomato)

def bfs():
    while q:
        tmp_x, tmp_y, tmp_z = q.popleft()
        for i in range(6):
            now_x = tmp_x + dx[i]
            now_y = tmp_y + dy[i]
            now_z = tmp_z + dz[i]
            
            if now_x < 0 or now_y < 0 or now_x >= n or now_y >= m or now_z < 0 or now_z >= h:
                continue
            if tomato[now_z][now_x][now_y] == 0:
                tomato[now_z][now_x][now_y] = tomato[tmp_z][tmp_x][tmp_y] + 1
                q.append([now_x, now_y, now_z])

for c in range(h):
    for a in range(n):
        for b in range(m):
            if tomato[c][a][b] == 1:
                q.append([a, b, c])

bfs()
ans = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 0:
                print(-1)
                exit()
            ans = tomato[k][i][j] if tomato[k][i][j] > ans else ans

print(ans - 1)
