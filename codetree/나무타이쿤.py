# 15:53

import sys

drug_moves = [(0, 1), (-1, 1), (-1, 0), (-1, -1),
              (0, -1), (1, -1), (1, 0), (1, 1)]
diag_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def input():
    return sys.stdin.readline().rstrip()


def ans():
    tmp = 0
    for i in MAP:
        tmp += sum(i)
    return tmp


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def move_drug_cords(dir, p):
    dy, dx = drug_moves[dir]
    for i in range(len(drugs_cords)):
        drugs_cords[i][0] = (drugs_cords[i][0] + dy * p) % n
        drugs_cords[i][1] = (drugs_cords[i][1] + dx * p) % n
    return


def increase_tree():
    for i in range(len(drugs_cords)):
        y, x = drugs_cords[i][0], drugs_cords[i][1]
        MAP[y][x] += 1
    for i in range(len(drugs_cords)):
        y, x = drugs_cords[i][0], drugs_cords[i][1]
        for dy, dx in diag_moves:
            ny, nx = y + dy, x + dx
            if not in_map(ny, nx):
                continue
            if MAP[ny][nx] >= 1:
                MAP[y][x] += 1
    return


def cut_tree_and_renew_drugs_cords():
    tmp = []

    for y in range(n):
        for x in range(n):
            if [y, x] in drugs_cords:
                continue
            if MAP[y][x] >= 2:
                MAP[y][x] -= 2
                tmp.append([y, x])

    return tmp


n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
drugs_cords = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
# 초기 특수 영양제는 n x n 격자의 좌하단의 4개의 칸에 주어집니다.
for times in range(m):
    dir, p = map(int, input().split())
    dir -= 1
    # 특수 영양제를 이동 규칙에 따라 이동시킵니다.
    move_drug_cords(dir, p)
    # print(drugs_cords)
    # 특수 영양제를 이동 시킨 후 해당 땅에 특수 영양제를 투입합니다. 투입 후 땅에 있던 특수 영양제는 사라지게 됩니다.
    increase_tree()
    drugs_cords = cut_tree_and_renew_drugs_cords()
    # 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 높이가 1 이상인 리브로수가 있는 만큼 높이가 더 성장합니다. 대각선으로 인접한 방향이 격자를 벗어나는 경우에는 세지 않습니다.

    # 특수 영양제를 투입한 리브로수를 제외하고 높이가 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로수로 특수 영양제를 사고, 해당 위치에 특수 영양제를 올려둡니다.
print(ans())
