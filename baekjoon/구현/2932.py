# 17:38

import sys


def input():
    return sys.stdin.readline().rstrip()


def make_map():
    MAP = [[0] * n for _ in range(n)]
    tmp = 1
    for i in range(n):
        for j in range(n):
            MAP[i][j] = tmp
            tmp += 1
    return MAP


def find_position(x):
    for i in range(n):
        for j in range(n):
            if MAP[i][j] == x:
                return i, j
    print("find position error")
    return


def row_rotate(y, x, r, c):
    # tmp_list = [0] * n
    cnt = 0
    if c == x:
        return cnt
    elif c > x:
        cnt = c - x
    else:
        cnt = n - (x - c)
    for _ in range(cnt):
        # swap
        tmp = MAP[y][0]
        for i in range(1, n):
            MAP[y][i], tmp = tmp, MAP[y][i]
        MAP[y][0] = tmp

    # for i in range(n):
    #     tmp_list[(i + cnt) % n] = MAP[y][i]
    # for i in range(n):
    #     MAP[y][i] = tmp_list[i]
    return cnt


def col_rotate(y, x, r, c):
    cnt = 0
    if r == y:
        return cnt
    elif r > y:
        cnt = r - y
    else:
        cnt = n - (y - r)

    for _ in range(cnt):
        # swap
        tmp = MAP[0][c]
        for i in range(1, n):
            MAP[i][c], tmp = tmp, MAP[i][c]
        MAP[0][c] = tmp

    # for i in range(n):
    #     tmp_list[(i + cnt) % n] = MAP[i][c]
    # for i in range(n):
    #     MAP[i][c] = tmp_list[i]
    return cnt


n, k = map(int, input().split())
MAP = make_map()
for round in range(k):
    ans = 0
    x, r, c = map(int, input().split())
    r -= 1
    c -= 1
    y, x = find_position(x)
    # 행 회전
    ans += row_rotate(y, x, r, c)
    # for i in MAP:
    #     print(i)
    # 열 회전
    ans += col_rotate(y, x, r, c)
    # print("now round", round)
    # for i in MAP:
    #     print(i)
    print(ans)
