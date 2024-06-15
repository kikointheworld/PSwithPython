# 20:05

import sys
from collections import deque
import heapq as hq


def input():
    return sys.stdin.readline().rstrip()


def check_finish():
    if target_r < r and target_c < c and MAP[target_r][target_c] == K:
        return True
    return False


def play_one():
    global MAP
    tmp_MAP = []
    max_len = 0
    for y in range(r):
        result_row = []

        tmp_dict = dict()
        for x in range(c):
            target = MAP[y][x]

            # 0은 무시하라는데용
            if target == 0:
                continue

            if target in tmp_dict:
                tmp_dict[target] += 1
            else:
                tmp_dict[target] = 1

        tmp_row = []

        for key in tmp_dict:
            tmp_row.append([tmp_dict[key], key])
        tmp_row.sort()

        cnt = 0
        for tmp_tmp_row in tmp_row:
            cnt += 1
            if cnt > 50:
                break
            result_row.append(tmp_tmp_row[1])
            result_row.append(tmp_tmp_row[0])

        max_len = max(max_len, cnt * 2)
        tmp_MAP.append(result_row)
    MAP = tmp_MAP

    # fill_zero
    for y in range(r):
        now_l = len(MAP[y])
        MAP[y] += [0] * (max_len - now_l)

    return max_len


def play_two():
    global MAP
    tmp_MAP = []
    max_len = 0
    for x in range(c):
        result_col = []
        tmp_dict = dict()
        for y in range(r):
            target = MAP[y][x]
            if target == 0:
                continue

            if target in tmp_dict:
                tmp_dict[target] += 1
            else:
                tmp_dict[target] = 1

        tmp_col = []

        for key in tmp_dict:
            tmp_col.append([tmp_dict[key], key])
        tmp_col.sort()

        cnt = 0
        for tmp_tmp_col in tmp_col:
            cnt += 1
            if cnt > 50:
                break
            result_col.append(tmp_tmp_col[1])
            result_col.append(tmp_tmp_col[0])
        max_len = max(max_len, cnt * 2)
        tmp_MAP.append(result_col)
    MAP = tmp_MAP

    # fill_zero
    for y in range(len(MAP)):
        now_l = len(MAP[y])
        MAP[y] += [0] * (max_len - now_l)

    return max_len


def rotate_MAP():
    global MAP
    tmp_MAP = [[0] * c for _ in range(r)]

    for y in range(c):
        for x in range(r):
            tmp_MAP[x][y] = MAP[y][x]

    MAP = tmp_MAP
    return


target_r, target_c, K = map(int, input().split())
target_r -= 1
target_c -= 1
MAP = [list(map(int, input().split())) for _ in range(3)]

r, c = 3, 3

time = 0
while (time <= 100):

    if check_finish():
        print(time)
        exit(0)

    if r >= c:
        c = play_one()

    else:
        r = play_two()
        rotate_MAP()
        # break
    # todo: 100넘어가는 경우 버리기

    time += 1
    # print()
    # print("now time: ", time, f"r: {r}, c: {c}")
    # for i in MAP:
    #     print(i)
    # print(r, c)


print(-1)
