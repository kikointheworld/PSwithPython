# 16:40 - 17:36

import sys
from collections import deque
from itertools import permutations


moves = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(z, y, x):
    return 0 <= z < 5 and 0 <= y < 5 and 0 <= x < 5


def rotate(graph):
    tmp = [[0] * 5 for _ in range(5)]
    for r in range(5):
        for c in range(5):
            tmp[c][4 - r] = graph[r][c]
    return tmp


def solve(graph):
    global ans
    # 탈출이 불가능함.
    if graph[0][0][0] == 0 or graph[4][4][4] == 0:
        return

    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0, 1))

    while (q):
        z, y, x, cnt = q.popleft()
        if z == 4 and y == 4 and x == 4:
            ans = min(ans, visited[4][4][4] - 1)
            return

        for dz, dy, dx in moves:
            nz, ny, nx = z + dz, y + dy, x + dx
            # 범위에 속하고 참가자가 들어갈 수 있는 칸
            if in_map(nz, ny, nx) and graph[nz][ny][nx] == 1:
                # 방문하지 않았거나 개선 가능
                if visited[nz][ny][nx] == 0 or visited[nz][ny][nx] > cnt + 1:
                    visited[nz][ny][nx] = cnt + 1
                    q.append((nz, ny, nx, cnt + 1))

    return


def make_rotate_cube_list():
    tmp = []
    now = [list(map(int, input().split())) for _ in range(5)]
    tmp.append(now)
    new = rotate(now)
    if new not in tmp:
        tmp.append(new)
    new = rotate(new)
    if new not in tmp:
        tmp.append(new)
    new = rotate(new)
    if new not in tmp:
        tmp.append(new)
    return tmp


cubes = []
for _ in range(5):
    cubes.append(make_rotate_cube_list())

ans = 10 ** 7
for i1, i2, i3, i4, i5 in permutations([0, 1, 2, 3, 4], 5):
    for one in cubes[i1]:
        for two in cubes[i2]:
            for three in cubes[i3]:
                for four in cubes[i4]:
                    for five in cubes[i5]:
                        solve([one, two, three, four, five])


print(-1 if ans == 10 ** 7 else ans)
