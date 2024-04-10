# 23:40 00:20

import sys
import heapq as hq
from collections import deque
EMPTY = -2
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def input():
    return sys.stdin.readline().rstrip()

def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


# -1은 검은색 0은 빨간색, 1 이상은 색깔

def make_bomb_list():
    visited = [[0] * n for _ in range(n)]
    my_hq = []
    for now_y in range(n - 1, -1, -1):
        for now_x in range(n):
            if MAP[now_y][now_x] >= 1 and not visited[now_y][now_x]:
                visited[now_y][now_x] = 1
                q = deque()
                q.append((now_y, now_x))
                now_color = MAP[now_y][now_x]
                cnt = 1
                rainbow_set = []
                while(q):
                    y, x = q.popleft()
                    for dy, dx in moves:
                        ny, nx = y + dy, x + dx
                        if not in_map(ny, nx):
                            continue
                        if visited[ny][nx] or MAP[ny][nx] < 0:
                            continue
                        if MAP[ny][nx] == now_color:
                            visited[ny][nx] = 1
                            q.append((ny, nx))
                            cnt += 1

                        elif MAP[ny][nx] == 0 and (ny, nx) not in rainbow_set:
                            rainbow_set.append((ny, nx))
                            cnt += 1
                            q.append((ny, nx))
                if cnt <= 1:
                    continue
                hq.heappush(my_hq, (-cnt, len(rainbow_set), -now_y, now_x))

    if len(my_hq) == 0:
        return False
    return list(hq.heappop(my_hq))

def bomb(bomb_list):
    global ans
    cnt, _, now_y, now_x = bomb_list
    ans += cnt ** 2
    now_y *= -1
    q = deque()
    q.append((now_y, now_x))
    color = MAP[now_y][now_x]
    MAP[now_y][now_x] = -2
    while(q):
        y, x = q.popleft()
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if not in_map(ny, nx):
                continue

            if MAP[ny][nx] == color or MAP[ny][nx] == 0:
                MAP[ny][nx] = EMPTY
                q.append((ny, nx))
    return

def gravity():
    for x in range(n):
        for y in range(n - 2, -1, -1):
            if MAP[y][x] <= -1:
                continue
            flag = False
            new_y = -1
            for j in range(y + 1, n):
                if MAP[j][x] == EMPTY:
                    flag = True
                    new_y = j
                else:
                    break
            if flag:
                MAP[y][x], MAP[new_y][x] = MAP[new_y][x], MAP[y][x]
    return

def rotate():
    tmp = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            tmp[y][x] = MAP[x][n - 1 - y]
    for y in range(n):
        for x in range(n):
            MAP[y][x] = tmp[y][x]


ans = 0
n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

while(True):
    bomb_list = make_bomb_list()
    if not bomb_list:
        break
    bomb(bomb_list)
    gravity()
    rotate()
    gravity()
print(ans)

"""
13 3
2 1 2 2 -1 0 3 2 1 -1 2 2 2 
-1 -1 3 0 0 1 1 -1 0 2 1 2 1 
3 1 2 1 3 3 3 0 2 2 1 2 2 
2 2 0 2 3 0 -1 3 1 0 1 1 -1 
0 3 0 2 2 3 2 3 0 0 2 1 0 
3 2 0 3 2 2 2 3 -1 2 0 3 1 
0 3 1 2 -1 2 2 -1 -1 3 3 -1 1 
3 0 -1 -1 -1 3 2 -1 -1 0 3 1 -1 
3 0 0 -1 3 3 -1 0 3 -1 3 2 3 
2 -1 3 0 1 -1 -1 1 2 0 1 -1 3 
-1 0 1 0 2 2 1 -1 0 3 0 -1 -1 
2 -1 0 2 0 1 -1 -1 3 2 0 -1 0 
1 1 2 0 3 2 0 1 0 3 -1 3 2 
"""

# 1806

