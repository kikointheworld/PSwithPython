# 16:38 16:51

import sys
import heapq as hq

moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def make_seat(now, now_fav_list):
    q = []

    for y in range(n):
        for x in range(n):
            # 항상 비어있는 칸으로 가야 한다.
            flag = True
            if MAP[y][x] != 0:
                flag = False
                continue

            empty = 0
            fav_cnt = 0
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if not in_map(ny, nx):
                    continue
                if MAP[ny][nx] == 0:
                    empty += 1
                    continue
                if MAP[ny][nx] in now_fav_list:
                    fav_cnt += 1
            if flag:
                hq.heappush(q, (-fav_cnt, -empty, y, x))

    _, _, y, x = hq.heappop(q)
    MAP[y][x] = now

    return


def ans():
    tmp = 0
    for y in range(n):
        for x in range(n):
            now = MAP[y][x]
            now_fav_list = fav_list[now]
            cnt = 0
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if not in_map(ny, nx):
                    continue
                if MAP[ny][nx] in now_fav_list:
                    cnt += 1

            if cnt == 0:
                continue
            tmp += 10 ** (cnt - 1)
    return tmp


n = int(input())
MAP = [[0] * n for _ in range(n)]
fav_list = [[] for _ in range((n**2) + 1)]

for _ in range(n ** 2):
    inputs = list(map(int, input().split()))
    now = inputs[0]
    now_fav_list = inputs[1:]
    fav_list[now] = now_fav_list
    make_seat(now, now_fav_list)


print(ans())
