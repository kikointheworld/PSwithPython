# 01:21

import sys
import heapq as hq
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 1 <= y <= n and 1 <= x <= n


def isAdjecent(y1, x1, y2, x2):
    if abs(y1 - y2) + abs(x1 - x2):
        return True
    else:
        return False


def solve(now, likes):
    now_q = []
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            # 칸이 비어있지 않음.
            if MAP[y][x] != 0:
                continue
            # (- 좋아하는 학생 수, - 인접한 칸 중에서 비어있는 칸 수, 행번호, 열번호 )
            likes_students_num, empty_num = 0, 0
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if not in_map(ny, nx):
                    continue

                if MAP[ny][nx] == 0:
                    empty_num += 1

                elif MAP[ny][nx] in likes:
                    likes_students_num += 1

            hq.heappush(now_q, (-likes_students_num, -empty_num, y, x))

    likes_students_num, empty_num, y, x = hq.heappop(now_q)
    MAP[y][x] = now
    return


n = int(input())
MAP = [[0] * (n + 1) for _ in range(n + 1)]
LIKES = [[] for _ in range((n ** 2) + 1)]
for _ in range(n ** 2):
    inputs = list(map(int, input().split()))
    now = inputs[0]
    likes = inputs[1:]
    solve(now, likes)
    LIKES[now] = likes

ans = 0

for i in MAP:
    print(i)

for y in range(1, n + 1):
    for x in range(1, n + 1):
        now = MAP[y][x]
        tmp = 0
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if not in_map(ny, nx):
                continue

            if MAP[ny][nx] in LIKES[now]:
                tmp += 1

        if tmp == 0:
            continue
        else:
            ans += 10 ** (tmp - 1)

print(ans)
