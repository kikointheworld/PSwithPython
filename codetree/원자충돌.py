# 15:43

import sys
from collections import deque
moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def input():
    return sys.stdin.readline().rstrip()

def atoms_move():
    while(atoms):
        y, x, mass, s, d = atoms.popleft()
        dy, dx = moves[d]
        ny, nx = (y + dy * s) % n, (x + dx * s) % n
        atoms_cords.add((ny, nx))
        MAP[ny][nx].append((mass, s, d))
    return

def atoms_integrate():
    tmp = deque()
    for y, x in atoms_cords:
        if len(MAP[y][x]) == 1:
            now_mass, now_speed, now_dir = MAP[y][x][0]
            tmp.append((y, x, now_mass, now_speed, now_dir))
            MAP[y][x].clear()
            continue
        total_mass, total_speed, is_diag, is_not_diag = 0, 0, 0, 0
        for i in range(len(MAP[y][x])):
            now_mass, now_speed, now_dir = MAP[y][x][i]
            total_mass += now_mass
            total_speed += now_speed
            if now_dir % 2 == 0:
                is_not_diag += 1
            else:
                is_diag += 1
        new_mass, new_speed = total_mass // 5, total_speed // len(MAP[y][x])
        if new_mass == 0:
            MAP[y][x].clear()
            continue
        # 상하좌우
        if is_diag == 0 or is_not_diag == 0:
            for i in range(4):
                tmp.append((y, x, new_mass, new_speed, i * 2))
        # 대각선
        else:
            for i in range(4):
                tmp.append((y, x, new_mass, new_speed, i * 2 + 1))
        MAP[y][x].clear()
    return tmp

def ans():
    tmp = 0
    # print(atoms)
    while(atoms):
        _, _, mass, _, _ = atoms.popleft()
        tmp += mass
    return tmp

n, m, k = map(int, input().split())
MAP = [[[] for _ in range(n)] for _ in range(n)]
atoms = deque()
for _ in range(m):
    y, x, mass, s, d = map(int, input().split())
    atoms.append((y - 1, x - 1, mass, s, d ))

for _ in range(k):
    atoms_cords = set()
    atoms_move()
    atoms = atoms_integrate()
#
# print(atoms_cords)
# for i in MAP:
#     print(i)
#
print(ans())