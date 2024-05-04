# 22:58

import sys
from collections import deque

moves = [(0, 1), (1, 0)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    if y == n - 1 and x == m - 1:
        return
    for dy, dx in moves:
        ny, nx = y + dy, x + dx
        if not in_map(ny, nx):
            continue
        if visited[ny][nx] or MAP[ny][nx] == 0:
            continue
        visited[ny][nx] = 1
        dfs(ny, nx)
    return


m, n = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
dfs(0, 0)

if visited[n - 1][m - 1] == 1:
    print("Yes")
else:
    print("No")
