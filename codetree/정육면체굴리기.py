# 17:21

import sys

# 동서북남
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]


class Dice:
    def __init__(self, top, bottom, left, right, front, back):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.front = front
        self.back = back

    def move(self, i):
        tmp_top, tmp_bottom, tmp_left, tmp_right, tmp_front, tmp_back = self.top, self.bottom, self.left, self.right, self.front, self.back
        if i == 0:  # 동
            self.bottom = tmp_right
            self.top = tmp_left
            self.left = tmp_bottom
            self.right = tmp_top
        elif i == 1:  # 서
            self.bottom = tmp_left
            self.top = tmp_right
            self.left = tmp_top
            self.right = tmp_bottom
        elif i == 2:  # 북
            self.bottom = tmp_back
            self.top = tmp_front
            self.front = tmp_bottom
            self.back = tmp_top
        elif i == 3:  # 남
            self.bottom = tmp_front
            self.top = tmp_back
            self.front = tmp_top
            self.back = tmp_bottom
        else:
            print("wrong i")


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < m


def change_dice_and_map(dice, y, x):
    if MAP[y][x] == 0:
        MAP[y][x] = dice.bottom
    else:
        dice.bottom = MAP[y][x]
        MAP[y][x] = 0

    return dice


def ROLL_THE_DICE(dice, dir, y, x):
    dy, dx = moves[dir]
    ny, nx = y + dy, x + dx
    # 격자를 벗어나면 아무일도 일어나지 않는다.
    if not in_map(ny, nx):
        return dice, y, x
    dice.move(dir)
    dice = change_dice_and_map(dice, ny, nx)
    print(dice.top)

    return dice, ny, nx


n, m, y, x, k = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
dice_dirs = list(map(int, input().split()))
for i in range(len(dice_dirs)):
    dice_dirs[i] -= 1
dice = Dice(0, 0, 0, 0, 0, 0)


dice = change_dice_and_map(dice, y, x)
for now_dir in dice_dirs:
    dice, y, x = ROLL_THE_DICE(dice, now_dir, y, x)
