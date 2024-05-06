# 23:01 - 23:51

import sys
from collections import deque

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n + 3 and 0 <= x < m


def checker(cords):
    for now_y, now_x in cords:
        if not in_map(now_y, now_x):
            return False
        if MAP[now_y][now_x] != 0:
            return False
    return True


def check_1(y, x):
    cords = [(y + 2, x), (y + 1, x - 1), (y + 1, x + 1)]
    return checker(cords)


def check_2(y, x):
    cords = [(y, x - 2), (y - 1, x - 1), (y + 1, x - 1),
             (y + 1, x - 2), (y + 2, x - 1)]
    return checker(cords)


def check_3(y, x):
    cords = [(y, x + 2), (y - 1, x + 1), (y + 1, x + 1),
             (y + 1, x + 2), (y + 2, x + 1)]
    return checker(cords)


def move_goylem(c, d):
    y, x = 1, c

    while (True):
        if check_1(y, x):
            y += 1
            continue
        if check_2(y, x):
            y += 1
            x -= 1
            d = (d - 1) % 4
            continue
        if check_3(y, x):
            y += 1
            x += 1
            d = (d + 1) % 4
            continue
        break

    return y, x, d


def clean_MAP():
    global MAP
    MAP = [[0] * m for _ in range(n + 3)]
    return


def get_ans(now_y, now_x):
    tmp = now_y
    q = deque()
    q.append((now_y, now_x))
    visited = [[0] * m for _ in range(n + 3)]
    visited[now_y][now_x] = 1

    while (q):
        y, x = q.popleft()
        tmp = max(tmp, y)
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if not in_map(ny, nx):
                continue
            if visited[ny][nx] or MAP[ny][nx] == 0:
                continue
            # 같은 세끼면 이동 가능 아니면 출구일 경우 이동 가능.
            if MAP[ny][nx] == MAP[y][x] or MAP[y][x] > 1000 or MAP[ny][nx] == 1000 + MAP[y][x]:
                visited[ny][nx] = 1
                q.append((ny, nx))
                continue
    return tmp - 2


n, m, k = map(int, input().split())
MAP = [[0] * m for _ in range(n + 3)]

# 0, 1, 2에 걸치면 안됨.

ans = 0
for now in range(1, k + 1):
    now_c, now_d = map(int, input().split())
    y, x, d = move_goylem(now_c - 1, now_d)

    # 골렘 최대치까지 왔으면 ans 추가 x
    if y <= 3:
        clean_MAP()
        continue

    for dy, dx in moves + [(0, 0)]:
        MAP[y + dy][x + dx] = now
    dy, dx = moves[d]
    MAP[y + dy][x + dx] = 1000 + now

    ans += get_ans(y, x)

print(ans)
