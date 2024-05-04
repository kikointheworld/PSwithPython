# 15:57 - 16:04
import sys
from collections import deque

moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < m


n, m = map(int, input().split())

MAP = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q = deque()

for i in range(m):
    if MAP[0][i] == '0':
        q.append((0, i))
        visited[0][i] = 1

while (q):
    y, x = q.pop()

    for dy, dx in moves:
        ny, nx = y + dy, x + dx
        if ny == n:
            print("YES")
            exit(0)
        if not in_map(ny, nx):
            continue
        if visited[ny][nx] or MAP[ny][nx] == '1':
            continue
        q.append((ny, nx))
        visited[ny][nx] = 1
print("NO")
