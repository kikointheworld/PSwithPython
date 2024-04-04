# 15:23 15:34 15:58

import sys
tree_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
salpo_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def get_inputs():
    n, m, k, c = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    ZECHO = [[0] * n for _ in range(n)]
    return n, m, k, c, MAP, ZECHO


def growth():
    for y in range(n):
        for x in range(n):
            if MAP[y][x] > 0:
                tmp = 0
                for dy, dx in tree_moves:
                    ny, nx = y + dy, x + dx
                    if not in_map(ny, nx):
                        continue
                    if MAP[ny][nx] > 0:
                        tmp += 1
                MAP[y][x] += tmp
    return


def reproduction():
    zecho_list = []
    for y in range(n):
        for x in range(n):
            if MAP[y][x] >= 1:
                now_list = []
                for dy, dx in tree_moves:
                    ny, nx = y + dy, x + dx
                    if not in_map(ny, nx):
                        continue
                    if MAP[ny][nx] == 0 and not ZECHO[ny][nx]:
                        now_list.append((ny, nx))
                offset = len(now_list)
                for ny, nx in now_list:
                    zecho_list.append((ny, nx, MAP[y][x] // offset))

    for y, x, cnt in zecho_list:
        MAP[y][x] += cnt

    return


def salpo_tree_num(y, x):
    tmp = MAP[y][x]

    for dy, dx in salpo_moves:
        for i in range(1, k + 1):
            ny, nx = y + dy * i, x + dx * i
            # 맵 밖을 나가거나
            if not in_map(ny, nx):
                break
            if MAP[ny][nx] == -1 or MAP[ny][nx] == 0:
                break
            tmp += MAP[ny][nx]

    return tmp


def salpo_cord():
    global total_ans
    ans, ans_y, ans_x = -1, -1, -1
    for y in range(n):
        for x in range(n):
            if MAP[y][x] == -1:
                continue

            if MAP[y][x] == 0:
                now_ans = 0

            else:
                now_ans = salpo_tree_num(y, x)
            if now_ans > ans:
                ans, ans_y, ans_x = now_ans, y, x
    total_ans += ans
    return ans_y, ans_x


def salpo():
    y, x = salpo_cord()
    if MAP[y][x] == 0:
        ZECHO[y][x] = c
        return
    MAP[y][x] = 0
    ZECHO[y][x] = c

    for dy, dx in salpo_moves:
        for i in range(1, k + 1):
            ny, nx = y + dy * i, x + dx * i
            # 맵 밖을 나가거나
            if not in_map(ny, nx):
                break
            if MAP[ny][nx] == -1:
                break
            if MAP[ny][nx] == 0:
                ZECHO[ny][nx] = c
                break
            MAP[ny][nx] = 0
            ZECHO[ny][nx] = c
    return


def remove_ZECHO():
    for y in range(n):
        for x in range(n):
            if ZECHO[y][x] >= 1:
                ZECHO[y][x] -= 1

    return


n, m, k, c, MAP, ZECHO = get_inputs()
total_ans = 0
c += 1
for _ in range(m):
    # 1. 성장
    growth()
    # 2. 번식
    reproduction()

    # 3. 제초제 살포
    salpo()

    # ZECHO cnt 줄여줌.
    remove_ZECHO()


print(total_ans)
