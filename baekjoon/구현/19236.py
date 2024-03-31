# 12:56

import sys
from collections import defaultdict
from copy import deepcopy


moves = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
ans = 0
MAP = [[[0, 0] for _ in range(5)] for _ in range(5)]
fish_dict = defaultdict()


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 1 <= y < 5 and 1 <= x < 5


def get_input():
    for i in range(1, 5):
        inputs = list(map(int, input().split()))
        for j in range(4):
            MAP[i][j + 1][0], MAP[i][j + 1][1] = inputs[j * 2], inputs[j * 2 + 1] % 8
            fish_dict[inputs[j * 2]] = (i, j + 1)


def fish_move(now_MAP, fish_dict, shark):
    shark_y, shark_x = shark

    for now in range(1, 17):
        if fish_dict[now] == -1:
            continue

        y, x = fish_dict[now]
        fish_value, fish_dir = now_MAP[y][x][0], now_MAP[y][x][1]

        for i in range(0, 8):
            now_fish_dir = (fish_dir + i) % 8
            dy, dx = moves[now_fish_dir]
            ny, nx = y + dy, x + dx

            # 이동 불가
            if not in_map(ny, nx):
                continue
            if shark_y == ny and shark_x == nx:
                continue

            # 이동 가능
            if now_MAP[ny][nx][0] == 0 and now_MAP[ny][nx][1] == 0:  # 빈칸이면 그냥 이동
                now_MAP[ny][nx][0], now_MAP[ny][nx][1] = fish_value, now_fish_dir
                now_MAP[y][x][0], now_MAP[y][x][1] = 0, 0
                fish_dict[fish_value] = (ny, nx)
                break

            # 물고기랑 자리 바꿈.
            tmp_value, tmp_dir = now_MAP[ny][nx][0], now_MAP[ny][nx][1]
            now_MAP[ny][nx][0], now_MAP[ny][nx][1] = fish_value, now_fish_dir
            fish_dict[fish_value] = (ny, nx)

            now_MAP[y][x][0], now_MAP[y][x][1] = tmp_value, tmp_dir
            fish_dict[tmp_value] = (y, x)
            break
    # exit(1)
    return


def backtracking(shark, shark_value, shark_dir, MAP, fish_dict):
    global ans
    ans = max(shark_value, ans)

    now_MAP = deepcopy(MAP)
    now_dict = deepcopy(fish_dict)

    # 물고기 이동은 상어 상관없이 이루어진다. 일단 물고기 이동.
    fish_move(now_MAP, now_dict, shark)

    # 이제 상어 움직일 차례
    shark_y, shark_x = shark
    dy, dx = moves[shark_dir % 8]

    for i in range(1, 4):
        ny, nx = shark_y + dy * i, shark_x + dx * i
        # 범위 지나가면 break
        if not in_map(ny, nx):
            break

        # 빈칸은 갈 수 없다.
        if now_MAP[ny][nx][0] == 0 and now_MAP[ny][nx][1] == 0:
            continue

        # 얘는 이제 먹혀야힘.
        tmp_value, tmp_dir = now_MAP[ny][nx][0], now_MAP[ny][nx][1]

        # now_MAP, now_dict 수정
        now_MAP[ny][nx][0], now_MAP[ny][nx][1] = 0, 0
        now_dict[tmp_value] = -1

        backtracking((ny, nx), shark_value + tmp_value,
                     tmp_dir, now_MAP, now_dict)

        # now_MAP, now_dict 복귀
        now_MAP[ny][nx][0], now_MAP[ny][nx][1] = tmp_value, tmp_dir
        now_dict[tmp_value] = (ny, nx)

    return


get_input()

# 상어 좌표, 값, 방향
shark, shark_value, shark_dir = (1, 1), MAP[1][1][0], MAP[1][1][1]
fish_dict[MAP[1][1][0]], MAP[1][1] = -1, [0, 0]
backtracking(shark, shark_value, shark_dir, MAP, fish_dict)

# for i in MAP:
#     print(i)

# for key in fish_dict:
#     print(key, fish_dict[key])
print(ans)
