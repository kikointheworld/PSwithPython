# 16:23 16:46

import sys
from collections import deque


# 기준은 시계방향
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Dice:

    def __init__(self, bottom, top, left, right, front, back):
        self.bottom = bottom
        self.top = top
        self.left = left
        self.right = right
        self.front = front
        self.back = back

    def move(self, i):
        if i == 0:
            tmp_bottom, tmp_top, tmp_left, tmp_right = self.bottom, self.top, self.left, self.right
            self.bottom = tmp_right
            self.top = tmp_left
            self.left = tmp_bottom
            self.right = tmp_top
        elif i == 1:
            tmp_bottom, tmp_top, tmp_front, tmp_back = self.bottom, self.top, self.front, self.back
            self.bottom = tmp_front  # type: ignore
            self.top = tmp_back
            self.front = tmp_top
            self.back = tmp_bottom
        elif i == 2:
            tmp_bottom, tmp_top, tmp_left, tmp_right = self.bottom, self.top, self.left, self.right
            self.bottom = tmp_left
            self.top = tmp_right
            self.left = tmp_top
            self.right = tmp_bottom
        elif i == 3:
            tmp_bottom, tmp_top, tmp_front, tmp_back = self.bottom, self.top, self.front, self.back
            self.bottom = tmp_back
            self.top = tmp_front
            self.front = tmp_bottom
            self.back = tmp_top
        else:
            print("EROOOR i >=5")


# 기준은 시계방향

def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def get_inputs():
    n, m = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    return n, m, MAP


def get_points(y, x):
    global ans
    num = 1
    value = MAP[y][x]
    visited = [[0] * n for _ in range(n)]
    visited[y][x] = 1
    q = deque()
    q.append((y, x))
    while (q):
        y, x = q.popleft()
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if not in_map(ny, nx):
                continue
            if visited[ny][nx]:
                continue
            if MAP[ny][nx] == value:
                visited[ny][nx] = 1
                num += 1
                q.append((ny, nx))
    ans += num * value

    return


def solve(dice, dice_dir):
    global dice_y, dice_x

    dy, dx = moves[dice_dir]
    ny, nx = dice_y + dy, dice_x + dx

    # 이럼 방향 바꿔서 이동.
    if not in_map(ny, nx):
        dice_dir = (dice_dir + 2) % 4
        dy, dx = moves[dice_dir]
        ny, nx = dice_y + dy, dice_x + dx

    # 다이스 위치 바꿔주고 다이스 회전시켜줌.
    dice_y, dice_x = ny, nx
    dice.move(dice_dir)

    # 점수 획득
    get_points(dice_y, dice_x)

    if MAP[dice_y][dice_x] < dice.bottom:
        dice_dir = (dice_dir + 1) % 4
    elif MAP[dice_y][dice_x] > dice.bottom:
        dice_dir = (dice_dir - 1 + 4) % 4

    return dice, dice_dir


ans = 0
dice_y, dice_x, dice_dir = 0, 0, 0
n, m, MAP = get_inputs()
dice = Dice(6, 1, 4, 3, 2, 5)

for _ in range(m):
    dice, dice_dir = solve(dice, dice_dir)

print(ans)
