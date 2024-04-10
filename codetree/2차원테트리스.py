# 13:55 14:44

import sys

def input():
    return sys.stdin.readline().rstrip()

def down1(y, x):
    MAP[y][x] = 1
    for now_y in range(y, 9):
        if MAP[now_y + 1][x] == 0:
            MAP[now_y + 1][x], MAP[now_y][x] = MAP[now_y][x], MAP[now_y + 1][x]
        else:
            break
    return

def right1(y, x):
    MAP[y][x] = 1
    for now_x in range(x, 9):
        if MAP[y][now_x + 1] == 0:
            MAP[y][now_x], MAP[y][now_x + 1] = MAP[y][now_x + 1], MAP[y][now_x]
        else:
            break
    return

def down2(y, x):
    MAP[y][x], MAP[y][x + 1] = 1, 1
    for now_y in range(y, 9):
        if MAP[now_y + 1][x] == 0 and MAP[now_y + 1][x + 1] == 0:
            MAP[now_y + 1][x], MAP[now_y][x] = MAP[now_y][x], MAP[now_y + 1][x]
            MAP[now_y + 1][x + 1], MAP[now_y][x + 1] = MAP[now_y][x + 1], MAP[now_y + 1][x + 1]
        else:
            break
    return

def right2(y, x):
    MAP[y][x], MAP[y][x + 1] = 1, 1
    for now_x in range(x, 8):
        if MAP[y][now_x + 2] == 0:
            MAP[y][now_x + 2], MAP[y][now_x + 1] = MAP[y][now_x + 1], MAP[y][now_x + 2]
            MAP[y][now_x + 1], MAP[y][now_x] = MAP[y][now_x], MAP[y][now_x + 1]
        else:
            break
    return

def down3(y, x):
    MAP[y][x], MAP[y + 1][x] = 1, 1
    for now_y in range(y + 1, 9):
        if MAP[now_y + 1][x] == 0:
            MAP[now_y][x], MAP[now_y + 1][x] = MAP[now_y + 1][x], MAP[now_y][x]
            MAP[now_y - 1][x], MAP[now_y][x] = MAP[now_y][x], MAP[now_y - 1][x]
        else:
            break

    return

def right3(y, x):
    MAP[y][x], MAP[y + 1][x]  = 1, 1
    for now_x in range(x, 9):
        if MAP[y][now_x + 1] == 0 and MAP[y + 1][now_x + 1] == 0:
            MAP[y][now_x], MAP[y][now_x + 1] = MAP[y][now_x + 1], MAP[y][now_x]
            MAP[y+1][now_x], MAP[y+1][now_x + 1] = MAP[y+1][now_x + 1], MAP[y+1][now_x]
        else:
            break
    return

def erase_yellow(y):
    for x in range(4):
        MAP[y][x] = 0
    return

def erase_red(x):
    for y in range(4):
        MAP[y][x] = 0
    return

def go_down(final_y):
    for x in range(4):
        for y in range(final_y - 1, 3, -1):
            MAP[y][x], MAP[y + 1][x] = MAP[y + 1][x], MAP[y][x]
    return


def go_right(final_x):
    for y in range(4):
        for x in range(final_x - 1, 3, -1):
            MAP[y][x + 1], MAP[y][x] = MAP[y][x], MAP[y][x + 1]
    return

def check_tetris():
    global ans
    for i in range(6, 10):
        if MAP[i][0] and MAP[i][1] and MAP[i][2] and MAP[i][3]:
            ans += 1
            erase_yellow(i)
            go_down(i)
        if MAP[0][i] and MAP[1][i] and MAP[2][i] and MAP[3][i]:
            ans += 1
            erase_red(i)
            go_right(i)
    return

def check_safety_zone():
    for _ in range(2):
        if MAP[5][0] or MAP[5][1] or MAP[5][2] or MAP[5][3]:
            erase_yellow(9)
            go_down(9)
        if MAP[0][5] or MAP[1][5] or MAP[2][5] or MAP[3][5]:
            erase_red(9)
            go_right(9)
MAP = [[0]* 10 for _ in range(10)]
k = int(input())
ans = 0
for tc in range(k):
    t, y, x = map(int, input().split())
    if t == 1:
        down1(y, x)
        right1(y, x)
    elif t == 2:
        down2(y, x)
        right2(y, x)

    else:
        down3(y, x)
        right3(y, x)
    check_tetris()
    check_safety_zone()



print(ans)
tmp = 0
for i in range(4):
    for j in range(6, 10):
        tmp += MAP[i][j]
        tmp += MAP[j][i]
print(tmp)
