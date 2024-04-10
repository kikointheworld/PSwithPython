# 17:17 18:19

import sys
from collections import deque

moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def input():
    return sys.stdin.readline().rstrip()

def in_map(y, x):
    return 0 <= y < n and 0 <= x < n

def rotate2(now_n, target_y, target_x):
    tmp = [[0] * now_n for _ in range(now_n)]

    for y in range(now_n):
        for x in range(now_n):
            tmp[x][now_n - 1 - y] = MAP[target_y + y][target_x + x]

    for y in range(now_n):
        for x in range(now_n):
            MAP[target_y + y][target_x + x] = tmp[y][x]
    return

def rotate(now_n, target_y, target_x):
    # print("now_n", now_n, "level", level)
    real_n = now_n // 2
    # 고정
    tmp = [[0] * now_n for _ in range(now_n)]

    for y in range(0, now_n, real_n):
        for x in range(0, now_n, real_n):
            # print("y", y, "x", x)
            for r in range(real_n):
                for c in range(real_n):
                    # print("r",r, "c",c)
                    # continue
                    tmp[x + r][now_n - 1 - y + c - real_n + 1] = MAP[target_y + y + r][target_x + x + c]


    # 고정
    for y in range(now_n):
        for x in range(now_n):
            MAP[target_y + y][target_x + x] = tmp[y][x]
    return

def MAP_rotate(level):
    now_n = 2 ** (level)
    l = n // now_n
    for y in range(0, l):
        for x in range(0, l):
            rotate(now_n, y * now_n, x * now_n)
    return

def melting_ice():
    tmp_list = []
    for y in range(n):
        for x in range(n):
            if MAP[y][x] == 0:
                continue
            tmp = 0
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if not in_map(ny, nx):
                    continue
                if MAP[ny][nx] > 0:
                    tmp += 1
            if tmp < 3:
                tmp_list.append((y, x))
    for y, x in tmp_list:
        MAP[y][x] -= 1
    return

def left_ice_sum():
    tmp = 0
    for i in MAP:
        tmp += sum(i)
    return tmp

def big_size():
    visited = [[0] * n for _ in range(n)]
    ans = 0
    for y in range(n):
        for x in range(n):
            if MAP[y][x] == 0 or visited[y][x]:
                continue
            visited[y][x] = 1
            q = deque()
            q.append((y, x))
            cnt = 1
            while(q):
                now_y, now_x = q.popleft()
                for dy, dx in moves:
                    ny, nx = now_y + dy, now_x + dx
                    if not in_map(ny,nx):
                        continue
                    if visited[ny][nx] or MAP[ny][nx] == 0:
                        continue
                    visited[ny][nx] = 1
                    q.append((ny,nx))
                    cnt += 1
            ans = max(ans, cnt)

    return ans

jisu_n, q = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(2 ** jisu_n)]
rotate_level_list = list(map(int, input().split()))
n = 2 ** jisu_n

for level in rotate_level_list:
    if level != 0:
        MAP_rotate(level)

    melting_ice()

print(left_ice_sum())
print(big_size())