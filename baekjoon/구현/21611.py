# 15:40 - 16:48

import sys
#  총 4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def map_printer():
    for i in MAP:
        print(i)
    return


def make_move_list():
    y, x = shark_y, shark_x

    tmp = [(y, x - 1),
           (y + 1, x - 1),
           (y + 1, x),
           (y + 1, x + 1),
           (y, x + 1),
           (y - 1, x + 1),
           (y - 1, x),
           (y - 1, x - 1)]

    cycle = (n - 3) // 2
    if cycle == 0:
        return tmp, len(tmp)
    # 1 - 4, 2 - 6, 3 - 8
    y, x = y - 1, x - 1
    for cycle_num in range(1, cycle + 1):
        x -= 1
        tmp.append((y, x))
        l = (cycle_num + 1) * 2
        for _ in range(1, l):
            y += 1
            tmp.append((y, x))
        for _ in range(l):
            x += 1
            tmp.append((y, x))
        for _ in range(l):
            y -= 1
            tmp.append((y, x))
        for _ in range(l):
            x -= 1
            tmp.append((y, x))

    return tmp, len(tmp)


def input():
    return sys.stdin.readline().rstrip()


def ball_move():
    now_index = 0
    next_index = 1
    while (True):
        now_y, now_x = move_list[now_index]

        # 스왑을 할 필요 없음.
        if MAP[now_y][now_x] != 0:
            now_index += 1
            next_index += 1
            continue
        # 스왑을 해줘야함.

        while (True):
            if next_index >= move_list_l:
                break
            next_y, next_x = move_list[next_index]

            # 다음 인덱스로 넘어가야함.
            if MAP[next_y][next_x] == 0:
                next_index += 1
                continue
            # swap
            MAP[next_y][next_x], MAP[now_y][now_x] = MAP[now_y][now_x], MAP[next_y][next_x]
            now_index += 1
            next_index += 1
            break
        if next_index >= move_list_l:
            break

    return


def ball_break(ball_break_list):
    for value, now_list in ball_break_list:
        for y, x in now_list:
            MAP[y][x] = 0
            ans[value] += 1

    return


def make_ball_break_list():
    ans = []
    flag = False
    now_value = -1
    now_list = []
    for i in range(move_list_l):
        y, x = move_list[i]
        value = MAP[y][x]
        if value == 0:
            break

        if now_value != value:
            if len(now_list) >= 4:
                ans.append((now_value, now_list))
            now_value = value
            now_list = [(y, x)]
        else:
            now_list.append((y, x))

    if len(now_list) >= 4:
        ans.append((now_value, now_list))

    return ans


def change_ball():
    tmp = []
    now_value = -1
    now_list = []
    for i in range(move_list_l):
        y, x = move_list[i]
        value = MAP[y][x]
        if MAP[y][x] == 0:
            break

        if value == now_value:
            now_list.append((y, x))
            continue

        # 첫 상태
        if now_value == -1:
            now_value = value
            now_list.append((y, x))
            continue
        tmp.append(len(now_list))
        tmp.append(now_value)
        now_value = value
        now_list = [now_value]
    if len(now_list) != 0:
        tmp.append(len(now_list))
        tmp.append(now_value)

    for i in range(min(len(tmp), move_list_l)):
        y, x = move_list[i]
        MAP[y][x] = tmp[i]

    return


def blizard(d, s):
    dy, dx = moves[d]

    # 얼음으로 구슬 파괴
    for i in range(1, s + 1):
        MAP[shark_y + dy * i][shark_x + dx * i] = 0
    # 구슬 이동
    ball_move()
    ball_break_list = make_ball_break_list()
    while (ball_break_list):
        ball_break(ball_break_list)
        ball_move()
        ball_break_list = make_ball_break_list()

    change_ball()

    return


ans = [0, 0, 0, 0]

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
shark_y, shark_x = ((n + 1) // 2) - 1, ((n + 1) // 2) - 1
move_list, move_list_l = make_move_list()

for _ in range(m):
    d, s = map(int, input().split())
    d -= 1
    blizard(d, s)

print(ans[1] + 2 * ans[2] + 3 * ans[3])
