# 15:42 - 17:22

import sys

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def get_input():
    n, m, k = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    shark_dir = [-1]
    for i in list(map(int, input().split())):
        shark_dir.append(i - 1)
    dir_priority = [[-1]]
    for _ in range(m):
        tmp = []
        for _ in range(4):
            tmptmp = []
            for i in list(map(int, input().split())):
                tmptmp.append(i - 1)
            tmp.append(tmptmp)
        dir_priority.append(tmp)

    SMELL = [[[0, 0] for _ in range(n)] for _ in range(n)]
    sharks_cord = [(-1, -1) for _ in range(m + 1)]

    for i in range(n):
        for j in range(n):
            if MAP[i][j] >= 1:
                sharks_cord[MAP[i][j]] = (i, j)

    return n, m, k, MAP, shark_dir, dir_priority, SMELL, sharks_cord


def spread_smell(sharks_cord, k):
    for i in range(1, m + 1):
        if sharks_cord[i] == (-1, -1):
            continue
        y, x = sharks_cord[i]
        SMELL[y][x][0], SMELL[y][x][1] = i, k
    return


def remove_smell():
    for y in range(n):
        for x in range(n):
            if SMELL[y][x][1] >= 1:
                SMELL[y][x][1] -= 1
                if SMELL[y][x][1] == 0:
                    SMELL[y][x][0] = 0
    return


def shark_move(now_shark):
    # 이미 죽은 상어
    if sharks_cord[now_shark] == (-1, -1):
        return
    y, x = sharks_cord[now_shark]
    now_dir = shark_dir[now_shark]
    # 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
    my_smell_cords = []
    for now_d in dir_priority[now_shark][now_dir]:
        dy, dx = moves[now_d]
        ny, nx = y + dy, x + dx
        if not in_map(ny, nx):
            continue
        # 냄새가 없다.
        if SMELL[ny][nx][0] == 0 and SMELL[ny][nx][1] == 0:
            shark_real_move(now_shark, y, x, ny, nx, now_d)
            # print(now_shark, ny, nx)
            return
        elif SMELL[ny][nx][0] == now_shark:
            my_smell_cords.append([y, x, ny, nx, now_d])

    shark_real_move(now_shark, my_smell_cords[0][0], my_smell_cords[0]
                    [1], my_smell_cords[0][2], my_smell_cords[0][3], my_smell_cords[0][4])

    return


def shark_real_move(now_shark, y, x, ny, nx, now_d):
    global left_shark
    shark_dir[now_shark] = now_d
    # 만약 빈 칸일 경우 그냥 원래 상어만 움직이면 됨
    if MAP[ny][nx] == 0:
        MAP[ny][nx], MAP[y][x] = now_shark, 0
        sharks_cord[now_shark] = (ny, nx)
        return

    # 만약 움직이려는 자리에 자기보다 작은 번호 상어가있으면 꺼져야함.
    if MAP[ny][nx] < now_shark:
        left_shark -= 1
        sharks_cord[now_shark] = (-1, -1)
        MAP[y][x] = 0
        shark_dir[now_shark] = -1
        dir_priority[now_shark] = [-1]
    else:
        origin_shark = MAP[ny][nx]
        MAP[ny][nx], MAP[y][x] = now_shark, 0
        sharks_cord[origin_shark] = (-1, -1)
        shark_dir[origin_shark] = -1
        dir_priority[origin_shark] = [-1]

        sharks_cord[now_shark] = (ny, nx)
        left_shark -= 1
    return


n, m, k, MAP, shark_dir, dir_priority, SMELL, sharks_cord = get_input()
left_shark = m
ans = 0


spread_smell(sharks_cord, k)
while (left_shark >= 2):
    if ans >= 1000:
        ans = -1
        break
    # 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
    for now_shark in range(1, m + 1):
        # 상어가 이동하면 MAP, shark_dir, sharks_cord바뀐다.
        shark_move(now_shark)
    remove_smell()
    spread_smell(sharks_cord, k)
    ans += 1

print(ans)
