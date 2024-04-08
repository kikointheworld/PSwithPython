# 21:17

import sys

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def input():
    return sys.stdin.readline().rstrip()

def in_map(y, x):
    return 0 <= y < n and 0 <= x < n
def get_inputs():
    n, m, k = map(int, input().split())
    player_MAP = [list(map(int, input().split())) for _ in range(n)]
    players_cords = [(-1, -1)] * (m + 1)
    for i in range(n):
        for j in range(n):
            if player_MAP[i][j] == 0:
                continue
            players_cords[player_MAP[i][j]] = (i, j)
    players_dir = [-1] * (m + 1)
    tmp = list(map(int, input().split()))
    for i in range(1, m + 1):
        players_dir[i] = tmp[i - 1] - 1
    players_dir_list = []
    players_dir_list.append([])
    for i in range(m):
        tmp = []
        for j in range(4):
            d1, d2, d3, d4 = map(int, input().split())
            tmp.append([d1 - 1, d2 - 1, d3 - 1, d4 - 1])
        players_dir_list.append(tmp)
    MAP = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for i in range(1, m + 1):
        y, x = players_cords[i]
        if y == -1 and x == -1:
            continue
        MAP[y][x][0], MAP[y][x][1] = i, k

    return n, m, k, players_cords, players_dir, players_dir_list, MAP, player_MAP

def monopolize():
    for now in range(1, m + 1):
        y, x = players_cords[now]
        if y == -1:
            continue
        MAP[y][x][0], MAP[y][x][1] = now, k + 1
    return

def only_one():
    for i in range(2, m + 1):
        y, x = players_cords[i]
        if y != -1:
            return False
    return True

def dir_calculate(dy, dx):
    if dy == -1:
        return 0
    elif dy == 1:
        return 1
    elif dx == -1:
        return 2
    else:
        return 3


def blank_move(now, y, x, ny, nx):
    players_cords[now] = (ny, nx)
    player_MAP[ny][nx] = now
    player_MAP[y][x] = 0
    players_dir[now] = dir_calculate(ny - y, nx - x)
    return

def battle_move(now, y, x, ny, nx):
    opp = player_MAP[ny][nx]
    # 내가 꺼져야함.
    if now > opp:
        player_MAP[y][x] = 0
        players_cords[now] = (-1, -1)
        players_dir[now] = -1
    else:
        player_MAP[y][x] = 0
        player_MAP[ny][nx] = now
        players_cords[opp] = (-1, -1)
        players_dir[opp] = -1
        players_cords[now] = (ny, nx)
        players_dir[now] = dir_calculate(ny - y, nx - x)

    return


def players_move():
    for now in range(1, m + 1):
        y, x = players_cords[now]
        if y == -1:
            continue
        dir = players_dir[now]
        now_moves = players_dir_list[now][dir]

        # 독점계약을 하지 않은 칸 찾기.
        find_blank = False
        last_my_y, last_my_x = -1, -1
        target_y, target_x = -1, -1
        # 아니라면 occupiedList에 추가해주기.
        for d_value in now_moves:
            dy, dx = moves[d_value]
            ny, nx = y + dy, x + dx
            if not in_map(ny, nx):
                continue
            # 독점계약을 하지 않은 칸을 찾음
            if MAP[ny][nx][0] == 0:
                target_y, target_x = ny, nx
                find_blank = True
                break
            # 이칸은 내칸.
            if MAP[ny][nx][0] == now:
                if last_my_y == -1:
                    last_my_y, last_my_x = ny, nx
        if find_blank:
            if player_MAP[target_y][target_x] != 0:
                battle_move(now, y, x, target_y, target_x)
            else:
                blank_move(now, y, x, target_y, target_x)
        else:
            blank_move(now, y, x, last_my_y, last_my_x)
    return

def remove_occupied():
    for i in range(n):
        for j in range(n):
            if MAP[i][j][1] >= 1:
                MAP[i][j][1] -= 1
                if MAP[i][j][1] == 0:
                    MAP[i][j][0] = 0
    return

n, m, k, players_cords, players_dir, players_dir_list, MAP, player_MAP = get_inputs()


now_turn = 0
while(True):
    now_turn += 1
    if now_turn > 1000:
        break
    players_move()
    monopolize()
    if only_one():
        break
    remove_occupied()

print(-1 if now_turn > 1000 else now_turn)