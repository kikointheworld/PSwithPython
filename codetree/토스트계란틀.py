# 21:32

import sys
from collections import deque

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


def input():
    return sys.stdin.readline().rstrip()


n, L, R = map(int, input().split())
n_squared = n * n
MAP = [list(map(int, input().split())) for _ in range(n)]

ans = 0


while (True):
    visited = [[0] * n for _ in range(n)]
    sum_list = [0]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                continue
            cnt += 1
            visited[y][x] = cnt
            q = deque()
            q.append((y, x))
            tmp_sum = MAP[y][x]
            tmp_cnt = 1
            while (q):
                now_y, now_x = q.popleft()
                for dy, dx in moves:
                    ny, nx = now_y + dy, now_x + dx
                    if not in_map(ny, nx):
                        continue
                    if not visited[ny][nx] and L <= abs(MAP[now_y][now_x] - MAP[ny][nx]) <= R:
                        q.append((ny, nx))
                        tmp_sum += MAP[ny][nx]
                        tmp_cnt += 1
                        visited[ny][nx] = cnt
            sum_list.append((tmp_sum // tmp_cnt))

    if cnt == n_squared:
        break
    ans += 1

    for y in range(n):
        for x in range(n):
            MAP[y][x] = sum_list[visited[y][x]]


# for i in visited:
#     print(i)

# print(sum_list)
print(ans)
