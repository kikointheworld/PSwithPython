# 17:28
import sys
from collections import deque
from itertools import permutations
import copy
MAX_DIS = 999
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def input():
    return sys.stdin.readline().rstrip()

def in_map(y, x):
    return 0 <= y < n and 0 <= x < m

def make_map(MAP):
    visited = [[-1] * m for _ in range(n)]
    cnt = -1
    for y in range(n):
        for x in range(m):
            if visited[y][x] >= 0:
                continue
            if MAP[y][x] == 0:
                continue
            cnt += 1
            visited[y][x] = cnt
            q = deque()
            q.append((y, x))

            while(q):
                now_y, now_x = q.popleft()
                for dy, dx in moves:
                    ny, nx = now_y + dy, now_x + dx
                    if not in_map(ny,nx):
                        continue
                    if visited[ny][nx] >= 0 or MAP[ny][nx] == 0:
                        continue
                    visited[ny][nx] = cnt
                    q.append((ny, nx))
    return visited, cnt

def make_graph(MAP, island_num):
    graph = [[MAX_DIS] * (island_num + 1) for _ in range(island_num + 1)]
    for y in range(n):
        for x in range(m):
            if MAP[y][x] == -1:
                continue
            now_island = MAP[y][x]
            for dy, dx in moves:
                for i in range(1, 11):
                    ny, nx = y + i * dy, x + i * dx
                    if not in_map(ny, nx):
                        break
                    if not MAP[ny][nx] == -1:
                        # 강이 끊긴거니 cnt를 구해서 graph 업데이트하자.
                        if i >= 3 and MAP[ny][nx] != now_island:
                            #새로운 땅일 것임.
                            graph[now_island][MAP[ny][nx]] = min(graph[now_island][MAP[ny][nx]], i - 1)
                            graph[MAP[ny][nx]][now_island] = min(graph[MAP[ny][nx]][now_island], i - 1)
                        break

    return graph

def backtracking(now, now_status, cnt):
    global ans
    if sum(now_status) == island_num + 1:
        ans = min(ans, cnt)
        return
    tmp = []

    for i in range(island_num + 1):
        if i == now:
            continue
        if now_status[i]:
            continue
        # 짜피 못감
        if graph[now][i] == MAX_DIS:
            continue
        tmp.append(i)

    for j in permutations(tmp):
        for i in j:
            now_status[i] = 1
            backtracking(i, now_status, cnt + graph[now][i])
            now_status[i] = 0


n, m = list(map(int, input().split()))
tmp = [list(map(int, input().split())) for _ in range(n)]
MAP, island_num = make_map(tmp)
graph = make_graph(MAP, island_num)

print("MAP")
for i in MAP:
    print(i)
print("GRAPH")
for i in graph:
    print(i)


ans = 10 ** 6
now_status = [0] * (island_num + 1)
for i in range(island_num + 1):
    now_status[i] = 1
    backtracking(i , now_status, 0)
    now_status[i] = 0

print(-1 if ans == 10 ** 6 else ans)

