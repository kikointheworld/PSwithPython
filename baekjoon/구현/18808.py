# 01:13 - 01:58

import sys

moves = [(0, 1), (1, 0)]


def input():
    return sys.stdin.readline().rstrip()


def angleCheck(r, c, sticker):
    if r <= n and c <= m:
        for i in range(n - r + 1):
            for j in range(m - c + 1):
                if isMatch(i, j, r, c, sticker):
                    fillIt(i, j, r, c, sticker)
                    return True
    return False


def isMatch(i, j, r, c, sticker):
    for y in range(r):
        for x in range(c):
            if sticker[y][x] == 1 and MAP[y + i][x + j] == 1:
                return False
    return True


def fillIt(i, j, r, c, sticker):
    global ans
    for y in range(r):
        for x in range(c):
            if sticker[y][x] == 1:
                MAP[y + i][x + j] = 1
                ans += 1
    return


def rotate(r, c, sticker):
    tmp = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            tmp[j][r - 1 - i] = sticker[i][j]

    return tmp


def solve(sticker):
    # 각 각도로 진행, 각 각도 전부 안맞으면 return 맞으면 뱉고..
    r, c = len(sticker), len(sticker[0])
    # 범위 초과 확인
    for i in range(4):
        if i != 0:
            sticker = rotate(r, c, sticker)
            r, c = c, r
        if angleCheck(r, c, sticker):
            return

    return


n, m, k = map(int, input().split())
MAP = [[0] * m for _ in range(n)]
stickers = []
ans = 0
for _ in range(k):
    r, _ = map(int, input().split())
    stickers.append([list(map(int, input().split())) for _ in range(r)])

for sticker in stickers:
    solve(sticker)

print(ans)
