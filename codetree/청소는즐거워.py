# 16:56

import sys
import math
# 하 우 상 좌
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

s_list = [[(2, 0, 0.05), (1, -1, 0.1), (0, -1, 0.07), (0, -2, 0.02), (-1, -1, 0.01), (1, 1, 0.1), (0, 1, 0.07), (0, 2, 0.02), (-1, 1, 0.01)],
          [(0, 2, 0.05), (-1, 1, 0.1), (-1, 0, 0.07), (-2, 0, 0.02), (-1, -1,
                                                                      0.01), (1, -1, 0.01), (1, 0, 0.07), (2, 0, 0.02), (1, 1, 0.1)],
          [(-2, 0, 0.05), (-1, -1, 0.1), (0, -1, 0.07), (0, -2, 0.02), (1, -
                                                                        1, 0.01), (-1, 1, 0.1), (0, 1, 0.07), (0, 2, 0.02), (1, 1, 0.01)],
          [(0, -2, 0.05), (-1, -1, 0.1), (-1, 0, 0.07), (-2, 0, 0.02), (-1, 1, 0.01), (1, -1, 0.1), (1, 0, 0.07), (2, 0, 0.02), (1, 1, 0.01)]]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def make_cords():
    y, x = n // 2, n // 2
    cords = [(y, x - 1, 3),
             (y + 1, x - 1, 0),
             (y + 1, x, 1),
             (y + 1, x + 1, 1),
             (y, x + 1, 2),
             (y - 1, x + 1, 2),
             (y - 1, x, 3),
             (y - 1, x - 1, 3)]
    if n == 3:
        return cords
    # 3 - 0, 5- 1, 7 - 2    4 6 8
    cnt = (n - 3) // 2
    y, x = y - 1, x - 1
    for now_cnt in range(cnt):
        l = (now_cnt + 2) * 2
        # 첫번쨰
        y, x = y, x - 1
        cords.append((y, x, 3))
        for i in range(l - 1):
            y, x = y + 1, x
            cords.append((y, x, 0))

        # 두번째는 오른쪽으로
        for i in range(l):
            y, x = y, x + 1
            cords.append((y, x, 1))

        # 세번째는 위쪽으로
        for i in range(l):
            y, x = y - 1, x
            cords.append((y, x, 2))

        # 네번째는 왼쪽으로
        for i in range(l):
            y, x = y, x - 1
            cords.append((y, x, 3))

    return cords


def sweap():
    global ans
    for y, x, dir in cords:
        dy, dx = moves[dir]
        target_y, target_x = y + dy, x + dx
        now_mungi = MAP[y][x]
        for dy, dx, p in s_list[dir]:
            ny, nx = y + dy, x + dx
            now_mungi -= math.floor(MAP[y][x] * p)
            if in_map(ny, nx):
                MAP[ny][nx] += math.floor(MAP[y][x] * p)
            else:
                ans += math.floor(MAP[y][x] * p)

        MAP[y][x] = 0
        if in_map(target_y, target_x):
            MAP[target_y][target_x] += now_mungi
        else:
            ans += now_mungi

    return


ans = 0
n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]
cords = make_cords()
sweap()
print(ans)
