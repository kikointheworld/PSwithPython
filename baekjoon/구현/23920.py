# 13:34 : 15:33

import sys
from collections import deque
import copy

fish_move_list = [(0, -1), (-1, -1), (-1, 0), (-1, 1),
                  (0, 1), (1, 1), (1, 0), (1, -1)]
# 상어움직임 상좌하우
shark_move_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
sharks_priority_list = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 1, 3], [0, 2, 0], [0, 2, 1], [0, 2, 2], [0, 2, 3], [0, 3, 0], [0, 3, 1], [0, 3, 2], [0, 3, 3], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 0, 3], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 0], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 3, 0], [1, 3, 1], [1, 3, 2], [
    1, 3, 3], [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 0, 3], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 0], [2, 2, 1], [2, 2, 2], [2, 2, 3], [2, 3, 0], [2, 3, 1], [2, 3, 2], [2, 3, 3], [3, 0, 0], [3, 0, 1], [3, 0, 2], [3, 0, 3], [3, 1, 0], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 2, 0], [3, 2, 1], [3, 2, 2], [3, 2, 3], [3, 3, 0], [3, 3, 1], [3, 3, 2], [3, 3, 3]]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < 4 and 0 <= x < 4


def ans():
    tmp = 0
    for i in MAP:
        for j in i:
            tmp += len(j)
    return tmp


def get_inputs():
    m, s = map(int, input().split())
    MAP = [[deque() for _ in range(4)] for _ in range(4)]
    SMELL = [[0] * 4 for _ in range(4)]

    for _ in range(m):
        y, x, dir = map(int, input().split())
        MAP[y - 1][x - 1].append((dir - 1, 0))
    shark_y, shark_x = map(int, input().split())
    shark_y -= 1
    shark_x -= 1
    return m, s, MAP, SMELL, shark_y, shark_x


def fish_move(round):
    for y in range(4):
        for x in range(4):
            if len(MAP[y][x]) == 0:
                continue
            tmp_q = deque()

            while (MAP[y][x]):

                fish_dir, fish_round = MAP[y][x].popleft()
                if fish_round == round:
                    tmp_q.append((fish_dir, fish_round))
                    continue

                # 이제 이동을 해주어야함.
                flag = False
                for i in range(0, -8, -1):
                    now_fish_dir = (fish_dir + i + 8) % 8

                    dy, dx = fish_move_list[now_fish_dir]
                    ny, nx = y + dy, x + dx

                    # 격자 밖이거나
                    if not in_map(ny, nx):
                        continue
                    # 상어가 있는 칸, 물고기의 냄새가 있는칸은 이동 불가
                    if (ny == shark_y and nx == shark_x) or SMELL[ny][nx] > 0:
                        continue

                    MAP[ny][nx].append((now_fish_dir, round))
                    flag = True
                    break
                if not flag:
                    tmp_q.append((fish_dir, round))

            while (tmp_q):
                MAP[y][x].append(tmp_q.popleft())

    return


def return_priority(now_list, depth):
    if depth == 3:
        sharks_priority_list.append(now_list)
        return
    for i in range(0, 4):
        return_priority(now_list + [i], depth + 1)
    return


def get_shark_priority(y, x):
    ans_num,  ans_i = -1, -1
    for i in range(64):
        # tmp = 0
        flag = True
        ny, nx = y, x
        visited = set()
        for j in range(3):
            which_to_go = sharks_priority_list[i][j]
            dy, dx = shark_move_list[which_to_go]
            ny, nx = ny + dy, nx + dx
            if not in_map(ny, nx):
                flag = False
                break
            visited.add((ny, nx))
        tmp = 0
        for ny, nx in visited:
            tmp += len(MAP[ny][nx])
        # 이러면 아예 못가는 거임.
        if flag == False:
            continue
        if tmp > ans_num:
            ans_num, ans_i = tmp, i

    return ans_i


def shark_move(index_i):
    global shark_y, shark_x
    move = sharks_priority_list[index_i]
    ny, nx = shark_y, shark_x
    for now_move in move:
        dy, dx = shark_move_list[now_move]
        ny, nx = ny + dy, nx + dx
        if MAP[ny][nx]:
            SMELL[ny][nx] = 3
        while (MAP[ny][nx]):
            MAP[ny][nx].pop()

        shark_y, shark_x = ny, nx

    return


def remove_smell():
    for y in range(4):
        for x in range(4):
            if SMELL[y][x] > 0:
                SMELL[y][x] -= 1
    return


def duplicate(duplicated_map, round):
    for y in range(4):
        for x in range(4):
            while (duplicated_map[y][x]):
                fish_dir, fish_round = duplicated_map[y][x].pop()
                MAP[y][x].append((fish_dir, round))

    return


m, s, MAP, SMELL, shark_y, shark_x = get_inputs()
# return_priority([], 0)
# print(sharks_priority_list)

for round in range(1, s + 1):
    # 상어가 모든 물고기에게 복제 마법을 시전한다. -> 5번에서 복제될 것임.
    duplicated_map = copy.deepcopy(MAP)
    fish_move(round)
    index_i = get_shark_priority(shark_y, shark_x)
    shark_move(index_i)
    remove_smell()
    duplicate(duplicated_map, round)
print(ans())
