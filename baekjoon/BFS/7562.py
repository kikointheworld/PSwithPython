'''
https://www.acmicpc.net/problem/7562
'''
from collections import deque

n = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(x, y):
    visited[x][y] = 1
    q = deque([[x, y, 0]])
    ans = 0
    while q:
        v = q.popleft()
        tmp_x = v[0]
        tmp_y = v[1]
        ans = v[2]
        if tmp_x == goal_x and tmp_y == goal_y:
            print(ans)
            return

        for j in range(8):
            now_x = tmp_x + dx[j]
            now_y = tmp_y + dy[j]            

            if now_x < 0 or now_y < 0 or now_x >= i or now_y >= i:
                pass
            elif visited[now_x][now_y] :
                pass
            else:
                visited[now_x][now_y] = 1
                tmp_ans = ans + 1
                q.append([now_x, now_y, tmp_ans])
        

for _ in range(n):
    i = int(input())
    visited = [[0] * i for _ in range(i)]
    x, y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    bfs(x, y)
