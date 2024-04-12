# 22:00 22:52

import sys
from collections import deque

moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def in_map(y, x):
    return 0 <= y < r and 0 <= x < c

def input():
    return sys.stdin.readline().rstrip()

def change_dir(dir):
    if dir == 0:
        return 1
    if dir == 1:
        return 0
    if dir == 2:
        return 3
    if dir == 3:
        return 2

def catch_shark(now_x):
    for y in range(r):
        if MAP[y][now_x]:
            now_num, now_s, now_d, now_z = MAP[y][now_x].popleft()
            sharks_cord[now_num] = (-1, -1)
            return now_z
    return 0

def shark_move(y, x, dir, s):
    dy, dx = moves[dir]
    ny, nx = y + dy * s, x + dx * s

    ny = ny % (2 * (r - 1))
    nx = nx % (2 * (c - 1))

    if 0 <= ny < r:
       pass
    else:
        ny = 2 * (r - 1) - ny
        dir = change_dir(dir)
    if 0 <= nx < c:
        pass
    else:
        nx = 2 * (c - 1) - nx
        dir = change_dir(dir)

    return ny, nx, dir

def left_one_shark(y, x):
    now_num, now_s, now_d, now_z = MAP[y][x].popleft()
    while(MAP[y][x]):
        new_num, new_s, new_d, new_z = MAP[y][x].popleft()
        if new_z > now_z:
            sharks_cord[now_num] = (-1, -1)
            now_num, now_s, now_d, now_z = new_num, new_s, new_d, new_z
        else:
            sharks_cord[new_num] = (-1, -1)

    MAP[y][x].append((now_num, now_s, now_d, now_z))
    return

def sharks_move():
    battle_set = set()
    for now_shark in range(m):
        y, x = sharks_cord[now_shark]
        if y == -1 and x == -1:
            continue
        now_num, now_s, now_d, now_z = MAP[y][x].popleft()
        if now_shark != now_num:
            print("SHARKS MOVE BUG")

        ny, nx, nd = shark_move(y, x, now_d, now_s)
        MAP[ny][nx].append((now_num, now_s, nd, now_z))
        battle_set.add((ny, nx))
        sharks_cord[now_num] = (ny, nx)

    # 다움직인듯?
    for y, x in battle_set:
        if len(MAP[y][x]) == 1:
            continue
        left_one_shark(y, x)

    return

r, c, m = map(int, input().split())
# 속력, 이동방향, 크기
sharks_cord = [(-1, -1)] * m
MAP = [[deque() for _ in range(c)] for _ in range(r)]
for shark_num in range(m):
    RR, CC, SS, DD, ZZ = map(int, input().split())
    MAP[RR - 1][CC - 1].append((shark_num, SS, DD - 1, ZZ))
    sharks_cord[shark_num] = (RR - 1, CC -1)

ans = 0
# print("시작 상태")
# for i in MAP:
#     print(i)
# 낚시왕은 움직일 거임.
for now_x in range(0, c):
    ans += catch_shark(now_x)
    sharks_move()
    # print("현재위치", now_x, "종료")
    # for i in MAP:
    #     print(i)
print(ans)