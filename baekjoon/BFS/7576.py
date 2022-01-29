'''
https://www.acmicpc.net/problem/7576
'''
from collections import deque
import sys

m, n = map(int,sys.stdin.readline().split())

tomato = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    tomato.append( list(map(int,sys.stdin.readline().split())))

q = deque()

def bfs():
    while q:
        tmp_x, tmp_y = q.popleft()
        for i in range(4):
            now_x = tmp_x + dx[i]
            now_y = tmp_y + dy[i]
            
            if now_x < 0 or now_y < 0 or now_x >= n or now_y >= m:
                continue
            if tomato[now_x][now_y] == 0:
                tomato[now_x][now_y] = tomato[tmp_x][tmp_y] + 1
                q.append([now_x, now_y])

for qw in range(n):
    for w in range(m):
        if tomato[qw][w] == 1:
            q.append([qw, w])
bfs()
ans = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        ans = tomato[i][j] if tomato[i][j] > ans else ans

print(ans - 1)
