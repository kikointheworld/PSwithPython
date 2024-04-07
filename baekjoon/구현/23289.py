# 3:36

import sys
from collections import deque

moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
wind_moves = [[[(0, 1)], [(-1, 0), (0, 1)], [(1, 0), (0, 1)]],
              [[(0, -1)],  [(-1, 0), (0, -1)], [(1, 0), (0, -1)]],
              [[(-1, 0)],  [(0, 1), (-1, 0)], [(0, -1), (-1, 0)]],
              [[(1, 0)],  [(0, 1), (1, 0)], [(0, -1), (1, 0)]]]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < r and 0 <= x < c


def is_wall(ny, nx, dy, dx):
    y, x = ny - dy, nx - dx
    if dy == -1 and dx == 0:
        if wall_MAP[y][x][0] == 1:
            return True
    elif dy == 1 and dx == 0:
        if wall_MAP[ny][nx][0] == 1:
            return True
    elif dy == 0 and dx == 1:
        if wall_MAP[y][x][1] == 1:
            return True
    elif dy == 0 and dx == -1:
        if wall_MAP[ny][nx][1] == 1:
            return True

    return False


def make_wind_list():
    visited = [[0] * c for _ in range(r)]
    visited_cnt = 0
    tmp_MAP = [[0] * c for _ in range(r)]

    for y in range(r):
        for x in range(c):
            if MAP[y][x] == 5:
                check_list.append((y, x))
                continue
            elif MAP[y][x] == 0:
                continue
            visited_cnt += 1
            dir = MAP[y][x] - 1
            dy, dx = moves[dir]
            ny, nx = y + dy, x + dx
            tmp_MAP[ny][nx] += 5
            visited[ny][nx] = visited_cnt
            q = deque()
            q.append((ny, nx, 5))

            while (q):
                now_y, now_x, cnt = q.popleft()
                if cnt <= 1:
                    continue
                for now_moves in wind_moves[dir]:
                    flag = True
                    ny, nx = now_y, now_x
                    for dy, dx in now_moves:
                        ny, nx = ny + dy, nx + dx
                        if not in_map(ny, nx):
                            flag = False
                            break
                        if is_wall(ny, nx, dy, dx) or visited[ny][nx] == visited_cnt:
                            flag = False
                            break

                    if flag:
                        visited[ny][nx] = visited_cnt
                        tmp_MAP[ny][nx] += cnt - 1
                        q.append((ny, nx, cnt - 1))
    for y in range(r):
        for x in range(c):
            if tmp_MAP[y][x] > 0:
                wind_list.append((y, x, tmp_MAP[y][x]))

    return


def wind():
    for y, x, v in wind_list:
        wind_MAP[y][x] += v
    return


def blend():
    tmp_list = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if not in_map(ny, nx):
                    continue
                if is_wall(ny, nx, dy, dx):
                    continue

                cnt = abs(wind_MAP[ny][nx] - wind_MAP[y][x]) // 4

                if wind_MAP[ny][nx] > wind_MAP[y][x]:
                    tmp_list[ny][nx] -= cnt
                    tmp_list[y][x] += cnt
                else:
                    tmp_list[ny][nx] += cnt
                    tmp_list[y][x] -= cnt

    for y in range(r):
        for x in range(c):
            wind_MAP[y][x] += tmp_list[y][x] // 2

    return


def out_wall_decrease():
    for x in range(c):
        if wind_MAP[0][x] > 0:
            wind_MAP[0][x] -= 1
        if wind_MAP[r - 1][x] > 0:
            wind_MAP[r - 1][x] -= 1
    for y in range(1, r - 1):
        if wind_MAP[y][0] > 0:
            wind_MAP[y][0] -= 1
        if wind_MAP[y][c - 1] > 0:
            wind_MAP[y][c - 1] -= 1

    return


def checker():
    for y, x in check_list:
        if wind_MAP[y][x] < k:
            return False

    return True


r, c, k = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
w = int(input())
walls = [list(map(int, input().split())) for _ in range(w)]
wind_MAP = [[0] * c for _ in range(r)]

wall_MAP = [[[0, 0] for _ in range(c)] for _ in range(r)]
for y, x, v in walls:
    wall_MAP[y-1][x-1][v] = 1
check_list = []
wind_list = []
chocolates = 0

make_wind_list()

while (True):
    wind()
    blend()
    out_wall_decrease()
    chocolates += 1
    if chocolates > 100:
        break
    if checker():
        break

print(chocolates)
