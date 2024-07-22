# 17:12
import sys
from collections import deque

moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def change_dir(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2


def move_horse(now):
    y, x = horse_cords[now]
    dy, dx = moves[horse_dir[now]]
    ny, nx = y + dy, x + dx

    moved_horse_num = []
    # 반대 방향 이동
    if not in_map(ny, nx):
        horse_dir[now] = change_dir(horse_dir[now])
        dy, dx = moves[horse_dir[now]]
        ny, nx = y + dy, x + dx

        if in_map(ny, nx) and MAP[ny][nx] != 2:
            # 흰색 격자인지
            if MAP[ny][nx] == 0:
                tmp_q = deque()
                while (True):
                    now_horse = horse_MAP[y][x].pop()
                    tmp_q.appendleft(now_horse)
                    moved_horse_num.append(now_horse)

                    if now_horse == now:
                        break
                horse_MAP[ny][nx] += tmp_q

            elif MAP[ny][nx] == 1:
                while (True):
                    now_horse = horse_MAP[y][x].pop()
                    horse_MAP[ny][nx].append(now_horse)
                    moved_horse_num.append(now_horse)
                    if now_horse == now:
                        break

    elif MAP[ny][nx] == 2:
        horse_dir[now] = change_dir(horse_dir[now])
        dy, dx = moves[horse_dir[now]]
        ny, nx = y + dy, x + dx

        if in_map(ny, nx) and MAP[ny][nx] != 2:
            # 흰색 격자인지
            if MAP[ny][nx] == 0:
                tmp_q = deque()
                while (True):
                    now_horse = horse_MAP[y][x].pop()
                    tmp_q.appendleft(now_horse)
                    moved_horse_num.append(now_horse)

                    if now_horse == now:
                        break
                horse_MAP[ny][nx] += tmp_q

            elif MAP[ny][nx] == 1:
                while (True):
                    now_horse = horse_MAP[y][x].pop()
                    horse_MAP[ny][nx].append(now_horse)
                    moved_horse_num.append(now_horse)
                    if now_horse == now:
                        break

    # 빨간색일 경우
    elif MAP[ny][nx] == 1:
        while (True):
            now_horse = horse_MAP[y][x].pop()
            horse_MAP[ny][nx].append(now_horse)
            moved_horse_num.append(now_horse)
            if now_horse == now:
                break

    # 흰색일 경우 그냥 움직임.
    else:
        tmp_q = deque()
        while (True):
            now_horse = horse_MAP[y][x].pop()
            tmp_q.appendleft(now_horse)
            moved_horse_num.append(now_horse)

            if now_horse == now:
                break
        horse_MAP[ny][nx] += tmp_q

    for i in moved_horse_num:
        horse_cords[i] = [ny, nx]

    # 종료 조건
    if in_map(ny, nx):
        if len(horse_MAP[ny][nx]) >= 4 or len(horse_MAP[y][x]) >= 4:
            print(ans)
            exit(0)

    return


n, k = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

horse_cords = []
horse_dir = []
horse_MAP = [[deque() for _ in range(n)] for _ in range(n)]


for horse_num in range(k):
    y, x, d = map(int, input().split())
    x, y, d = x - 1, y - 1, d - 1
    horse_cords.append([y, x])
    horse_dir.append(d)
    horse_MAP[y][x].append(horse_num)


ans = 1

while (True):
    # if 말이 4개가 겹친다면.

    for horse_num in range(k):
        move_horse(horse_num)

    if ans > 1000:
        print(-1)
        break

    ans += 1


'''
6 7
2 0 0 2 2 2 
1 2 0 2 2 1 
0 1 0 0 1 0 
0 1 0 1 0 2 
2 0 0 0 0 2 
1 0 0 0 1 0 
6 6 3
3 6 2
1 2 3
4 2 4
2 2 3
6 2 4
6 5 4

'''
