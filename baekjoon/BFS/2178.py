'''
https://www.acmicpc.net/problem/2178
'''

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, c):
    q = deque([[a, b, c]])

    while q:    
        tmp = q.popleft()
        x = tmp[0]
        y = tmp[1]
        ans = tmp[2]

        if isVisited[x][y]:
            continue
        
        if graph[x][y] == 0:
            continue
            
        isVisited[x][y] = 1

        if x == n - 1 and y == m - 1:
            print(ans)
            return
        
        for i in range(4):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]

            if tmp_x < 0 or tmp_y < 0 or tmp_x >= n or tmp_y >= m:
                continue

            q.append([tmp_x, tmp_y, ans + 1])




n, m = map(int, input().split())

graph = []

isVisited = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input())))

bfs(0, 0, 1)
