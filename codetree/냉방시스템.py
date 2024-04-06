# 16:36

import sys
from collections import deque

moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]
aircon_moves = [[[(0, -1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]],
                [[(-1, 0)], [(0, 1), (-1, 0)], [(0, -1), (-1, 0)]],
                [[(0, 1)], [(1, 0), (0, 1)], [(-1, 0), (0, 1)]],
                [[(1, 0)], [(0, -1), (1, 0)], [(0, 1), (1, 0)]]]


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def input():
    return sys.stdin.readline().rstrip()

# 0 은 빈 공간, 1은 사무실, 2는 왼쪽에어컨, 3은 위, 4는 오른쪽, 5는 아래
# 0 왼쪽, 1 위쪽, 2 오른쪽, 3 아래


def get_inputs():
    n, m, k = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    wall_MAP = [[[0, 0] for _ in range(n)] for _ in range(n)]
    office_cords = []
    for _ in range(m):
        y, x, v = map(int, input().split())
        wall_MAP[y - 1][x - 1][v] = 1

    aircon_cords = []

    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 0:
                continue
            if MAP[i][j] == 1:
                office_cords.append((i, j))
            else:
                aircon_cords.append((i, j, MAP[i][j] - 2))

    return n, m, k, MAP, office_cords, wall_MAP, aircon_cords


def satisfied():
    for y, x in office_cords:
        if cool_MAP[y][x] < k:
            return False
    return True


def is_wall(ny, nx, dy, dx):
    # dy, dx = moves[dir]
    y, x = ny - dy, nx - dx
    if dy == 0 and dx == -1:
        if wall_MAP[y][x][1] == 1:
            return True
    elif dy == -1 and dx == 0:
        if wall_MAP[y][x][0] == 1:
            return True
    elif dy == 0 and dx == 1:
        if wall_MAP[ny][nx][1] == 1:
            return True
    elif dy == 1 and dx == 0:
        if wall_MAP[ny][nx][0] == 1:
            return True
    else:
        print("WRONG WALL DIR INPUT in wall_check function")

    return False


def make_cool(aircon_y, aircon_x, dir, visit_value):
    now_moves = aircon_moves[dir]
    dy, dx = moves[dir]
    ny, nx = aircon_y + dy, aircon_x + dx
    # 시작부터 막혀있으면 안되잖슴.
    # if not in_map(ny, nx):
    #     return
    # if is_wall(ny, nx, dy, dx):
    #     return

    q = deque()
    q.append((ny, nx, 5))
    visited[ny][nx] = visit_value
    cool_MAP[ny][nx] += 5
    while (q):
        y, x, cnt = q.popleft()
        if cnt <= 1:
            continue
        for now_move in now_moves:
            ny, nx = y, x
            flag = True
            for dy, dx in now_move:
                ny, nx = ny + dy, nx + dx
                if not in_map(ny, nx):
                    flag = False
                    break
                if is_wall(ny, nx, dy, dx):
                    flag = False
                    break
            # 갈수없거나 이미 방문한 경우,
            if not flag or visited[ny][nx] == visit_value:
                continue

            visited[ny][nx] = visit_value
            cool_MAP[ny][nx] += cnt - 1
            q.append((ny, nx, cnt - 1))
    return


def blend_air():
    tmp = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if not in_map(ny, nx):
                    continue
                if is_wall(ny, nx, dy, dx):
                    continue

                value = (abs(cool_MAP[ny][nx] - cool_MAP[y][x]) // 4)
                if value == 0:
                    continue

                if cool_MAP[ny][nx] > cool_MAP[y][x]:
                    tmp[ny][nx] -= value
                    tmp[y][x] += value
                else:
                    tmp[ny][nx] += value
                    tmp[y][x] -= value

    for y in range(n):
        for x in range(n):
            cool_MAP[y][x] += tmp[y][x] // 2

    return


def outwall_act():
    for x in range(n):
        if cool_MAP[0][x] >= 1:
            cool_MAP[0][x] -= 1
        if cool_MAP[n - 1][x] >= 1:
            cool_MAP[n - 1][x] -= 1
    for y in range(1, n - 1):
        if cool_MAP[y][0] >= 1:
            cool_MAP[y][0] -= 1
        if cool_MAP[y][n - 1] >= 1:
            cool_MAP[y][n - 1] -= 1
    return


n, m, k, MAP, office_cords, wall_MAP, aircon_cords = get_inputs()
cool_MAP = [[0] * n for _ in range(n)]
times = 0

while (not satisfied() and times <= 100):
    visited = [[0] * n for _ in range(n)]
    cnt = 1
    for aircon_y, aircon_x, dir in aircon_cords:
        make_cool(aircon_y, aircon_x, dir, cnt)
        cnt += 1

    # print("make_cool이후")
    # for i in cool_MAP:
    #     print(i)

    blend_air()
    # print("blend_air 이후")
    # for i in cool_MAP:
    #     print(i)

    outwall_act()
    # print("outwall_act 이후")

    times += 1

print(times if times != 101 else -1)
