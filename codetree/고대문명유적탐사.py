# 19:03 19:39

import sys
import heapq as hq
from collections import deque

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < 5 and 0 <= x < 5


def rotate_90(start_y, start_x):
    tmp = [[0] * 3 for _ in range(3)]

    for y in range(3):
        for x in range(3):
            tmp[x][3 - 1 - y] = MAP[start_y + y][start_x + x]

    for y in range(3):
        for x in range(3):
            MAP[start_y + y][start_x + x] = tmp[y][x]
    return


def rotate_180(start_y, start_x):
    tmp = [[0] * 3 for _ in range(3)]

    for y in range(3):
        for x in range(3):
            tmp[3 - 1 - y][3 - 1 - x] = MAP[start_y + y][start_x + x]

    for y in range(3):
        for x in range(3):
            MAP[start_y + y][start_x + x] = tmp[y][x]
    return


def rotate_270(start_y, start_x):
    tmp = [[0] * 3 for _ in range(3)]

    for y in range(3):
        for x in range(3):
            tmp[3 - 1 - x][y] = MAP[start_y + y][start_x + x]

    for y in range(3):
        for x in range(3):
            MAP[start_y + y][start_x + x] = tmp[y][x]
    return


def calculate_value():
    tmp = 0
    visited = [[0] * 5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            if visited[y][x]:
                continue
            visited[y][x] = 1
            value = MAP[y][x]
            q = deque()
            q.append((y, x))
            cnt = 1
            while (q):
                now_y, now_x = q.popleft()
                for dy, dx in moves:
                    ny, nx = now_y + dy, now_x + dx
                    if not in_map(ny, nx):
                        continue
                    if visited[ny][nx] or MAP[ny][nx] != value:
                        continue
                    visited[ny][nx] = 1
                    cnt += 1
                    q.append((ny, nx))
            if cnt >= 3:
                tmp += cnt

    return tmp


def get_rotate_hq():
    now_hq = []
    for y in range(3):
        for x in range(3):
            for i in range(3):
                rotate_90(y, x)
                tmp_ans = calculate_value()
                if tmp_ans > 0:
                    hq.heappush(now_hq, (-tmp_ans, i, x, y))
            rotate_90(y, x)  # 원상복구
    if len(now_hq) == 0:
        return -1, -1, -1, -1
    tmp_ans, i, x, y = hq.heappop(now_hq)

    return -1 * tmp_ans, i, x, y


def rotate_map(i, y, x):
    if i == 0:
        rotate_90(y, x)
    elif i == 1:
        rotate_180(y, x)
    else:
        rotate_270(y, x)
    return


def remove_and_fill():
    tmp = 0
    now_hq = []
    visited = [[0] * 5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            if visited[y][x]:
                continue
            value = MAP[y][x]
            cnt = 1
            visited[y][x] = 1
            q = deque()
            q.append((y, x))
            tmp_list = [(y, x)]
            while (q):
                now_y, now_x = q.popleft()
                for dy, dx in moves:
                    ny, nx = now_y + dy, now_x + dx
                    if not in_map(ny, nx):
                        continue
                    if visited[ny][nx] or MAP[ny][nx] != value:
                        continue
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    tmp_list.append((ny, nx))
                    cnt += 1
            if cnt >= 3:
                tmp += cnt
                for now_y, now_x in tmp_list:
                    hq.heappush(now_hq, (now_x, -now_y))

    while (now_hq):
        now_x, now_y = hq.heappop(now_hq)
        now_y = -1 * now_y
        value = rests.popleft()
        MAP[now_y][now_x] = value
    return tmp


k, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(5)]
rests = deque(list(map(int, input().split())))

for _ in range(k):
    ans = 0
    tmp_ans, i, x, y = get_rotate_hq()
    # print(" tmp_ans, i, x, y",  tmp_ans, i, x, y)
    if tmp_ans == -1:
        break
    rotate_map(i, y, x)
    ans += tmp_ans
    remove_and_fill()
    while (True):
        tmp_ans = remove_and_fill()
        if tmp_ans == 0:
            break
        ans += tmp_ans
    print(ans, end=' ')
print()
