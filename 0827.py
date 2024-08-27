# 16:25
import sys
import copy

def input():
    return sys.stdin.readline().rstrip()

def return_max(MAP):
    global ans
    for i in MAP:
        ans = max(ans, max(i))
    return 

def up(MAP):
    visited = [[0] * n for _ in range(n)]
    for y in range(1, n):
        for x in range(n):
            now = MAP[y][x]
            for k in range(y - 1, -1, -1):
                new = MAP[k][x]
                if new == 0:
                    if k == 0:
                        MAP[y][x] = 0
                        MAP[0][x] = now
                        break
                    continue

                if now == new:
                    if visited[k][x] == 1:
                        MAP[y][x] = 0
                        MAP[k + 1][x] = now
                    else:
                        visited[k][x] = 1
                        MAP[k][x] *= 2
                        MAP[y][x] = 0
                    break
                else:
                    MAP[y][x] = 0
                    MAP[k + 1][x] = now
                    break
    return 

def left(MAP):
    visited = [[0] * n for _ in range(n)]
    for x in range(1, n):
        for y in range(n):
            now = MAP[y][x]
            for k in range(x - 1, -1, -1):
                new = MAP[y][k]
                if new == 0:
                    if k == 0:
                        MAP[y][x] = 0
                        MAP[y][0] = now
                        break
                    continue

                if now == new:
                    if visited[y][k] == 1:
                        MAP[y][x] = 0
                        MAP[y][k + 1] = now
                    else:
                        visited[y][k] = 1
                        MAP[y][k] *= 2
                        MAP[y][x] = 0
                    break
                else:
                    MAP[y][x] = 0
                    MAP[y][k + 1] = now
                    break
    return

def down(MAP):
    visited = [[0] * n for _ in range(n)]
    for y in range(n - 2, -1, -1):
        for x in range(n):
            now = MAP[y][x]
            for k in range(y + 1, n):
                new = MAP[k][x]
                if new == 0:
                    if k == n - 1:
                        MAP[y][x] = 0
                        MAP[k][x] = now
                        break
                    continue

                if now == new:
                    if visited[k][x] == 1:
                        MAP[y][x] = 0
                        MAP[k - 1][x] = now
                    else:
                        visited[k][x] = 1
                        MAP[k][x] *= 2
                        MAP[y][x] = 0
                    break
                else:
                    MAP[y][x] = 0
                    MAP[k - 1][x] = now
                    break
    return 

def right(MAP):
    visited = [[0] * n for _ in range(n)]
    for x in range(n - 2, -1, -1):
        for y in range(n):
            now = MAP[y][x]
            for k in range(x + 1, n):
                new = MAP[y][k]
                if new == 0:
                    if k == n - 1:
                        MAP[y][x] = 0
                        MAP[y][k] = now
                        break
                    continue

                if now == new:
                    if visited[y][k] == 1:
                        MAP[y][x] = 0
                        MAP[y][k - 1] = now
                    else:
                        visited[y][k] = 1
                        MAP[y][k] *= 2
                        MAP[y][x] = 0
                    break
                else:
                    MAP[y][x] = 0
                    MAP[y][k - 1] = now
                    break
    return 

def back_tracking(now_map, cnt):
    if cnt > 5:
        return
    return_max(now_map)
    new_map = copy.deepcopy(now_map)
    up(new_map)
    back_tracking(new_map, cnt + 1)

    new_map = copy.deepcopy(now_map)
    down(new_map)
    back_tracking(new_map, cnt + 1)

    new_map = copy.deepcopy(now_map)
    left(new_map)
    back_tracking(new_map, cnt + 1)

    new_map = copy.deepcopy(now_map)
    right(new_map)
    back_tracking(new_map, cnt + 1)

    return
    



ans = -1
n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

back_tracking(MAP, 0)

print(ans)
