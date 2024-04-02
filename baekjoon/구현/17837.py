# 19:34 - 20:08

import sys
from collections import deque

moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def change_dir(dir):
    if dir == 0:
        return 3
    elif dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 0


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def input():
    return sys.stdin.readline().rstrip()


def horse_move(now_horse):
    y, x = horse_cord[now_horse]
    dy, dx = moves[horse_dir[now_horse]]
    ny, nx = y + dy, x + dx
    # 체스판을 벗어나는 경우
    # 이동하려는 칸이 파란색인 경우
    if (in_map(ny, nx) and colorMAP[ny][nx] == 2) or not in_map(ny, nx):
        # 말의 이동방향을 반대로 한다.
        horse_dir[now_horse] = change_dir(horse_dir[now_horse])
        ny, nx = y - dy, x - dx

    # 그래도 칸이 벗어나면...
    if not in_map(ny, nx):
        return

    # 다음 칸도 파란색이라면.. 가만히 있는다.
    if colorMAP[ny][nx] == 2:
        return

    # 이동하려는 칸이 흰색인 경우
    if colorMAP[ny][nx] == 0:
        move_horse_list = deque()
        while (MAP[y][x]):
            last = MAP[y][x].pop()
            move_horse_list.appendleft(last)
            if last == now_horse:
                break

        while (move_horse_list):
            now = move_horse_list.popleft()
            horse_cord[now] = (ny, nx)
            MAP[ny][nx].append(now)

        if len(MAP[ny][nx]) >= 4:
            print(turn)
            exit(0)
        return

    # 이동하려는 칸이 빨간색인 경우
    if colorMAP[ny][nx] == 1:
        move_horse_list = deque()
        while (MAP[y][x]):
            last = MAP[y][x].pop()
            move_horse_list.appendleft(last)
            if last == now_horse:
                break

        while (move_horse_list):
            now = move_horse_list.pop()
            horse_cord[now] = (ny, nx)
            MAP[ny][nx].append(now)

        if len(MAP[ny][nx]) >= 4:
            print(turn)
            exit(0)
        return

    return


n, k = map(int, input().split())
# 0은 흰색, 1은 빨간색, 2는 파란색
colorMAP = [list(map(int, input().split())) for _ in range(n)]
MAP = [[deque() for _ in range(n)] for _ in range(n)]
horse_cord = [(-1, -1)] * (k + 1)
horse_dir = [-1] * (k + 1)
for now_horse in range(1, k + 1):
    r, c, dir = map(int, input().split())
    MAP[r - 1][c - 1].append(now_horse)
    horse_dir[now_horse] = dir % 4
    horse_cord[now_horse] = (r - 1, c - 1)

turn = 1
while (True):
    if turn > 1000:
        print(-1)
        break
    for now_horse in range(1, k + 1):
        horse_move(now_horse)

    turn += 1
