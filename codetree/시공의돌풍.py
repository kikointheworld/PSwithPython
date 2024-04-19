# 19:11
moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]

from itertools import combinations

n, m, t = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

def in_map(y, x):
    return 0 <= y < n and 0 <= x < m

def spread():
    tmp = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if x == 0:
                if y == up_y or y == down_y:
                    continue
            spread_value = MAP[y][x] // 5
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if nx == 0:
                    if ny == up_y or ny == down_y:
                        continue
                if not in_map(ny, nx):
                    continue
                tmp[ny][nx] += spread_value
                MAP[y][x] -= spread_value
    for y in range(n):
        for x in range(m):
            MAP[y][x] += tmp[y][x]

    return

def clean_up():
    tmp = 0
    for x in range(1, m):
        MAP[up_y][x], tmp = tmp, MAP[up_y][x]
    for y in range(up_y - 1, -1, -1):
        MAP[y][m - 1], tmp = tmp, MAP[y][m - 1]
    for x in range(m - 2, -1, -1):
        MAP[0][x], tmp = tmp, MAP[0][x]
    for y in range(1, up_y):
        MAP[y][0], tmp = tmp, MAP[y][0]
    return


def clean_down():
    tmp = 0
    for x in range(1, m):
        MAP[down_y][x], tmp = tmp, MAP[down_y][x]
    for y in range(down_y + 1, n):
        MAP[y][m - 1], tmp = tmp, MAP[y][m-1]
    for x in  range(m - 2, -1, -1):
        MAP[n - 1][x], tmp = tmp, MAP[n-1][x]
    for y in range(n - 2, down_y, -1):
        MAP[y][0], tmp = tmp, MAP[y][0]

    return

up_y, up_x = -1, 0
down_y, down_x = -1, 0

for y in range(n):
    if MAP[y][0] == -1:
        up_y = y
        down_y = y + 1
        break

for now_time in range(1, t + 1):
    spread()
    clean_up()
    clean_down()


ans = 2
for i in MAP:
    # print(i)
    ans += sum(i)
print(ans)
