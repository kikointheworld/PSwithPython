# 18:50

from collections import deque

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())

def in_map(y, x):
    return 0 <= y < n and 0 <= x < n

def combinations(arr, cnt):
    if len(arr) == m:
        COMB.append(arr)
        return
    for i in range(cnt + 1, l):
        combinations(arr + [i], i)
    return

def solve(cords):
    global time
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    for c in cords:
        y, x = hospital_cord[c]
        visited[y][x] = 0
        q.append((y, x, 0))

    tmp_virus = 0
    max_time = -1
    while(q):
        y, x, cnt = q.popleft()
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if not in_map(ny, nx):
                continue
            if visited[ny][nx] != -1 or MAP[ny][nx] == 1:
                continue
            if MAP[ny][nx] == 0:
                tmp_virus += 1
                max_time = max(max_time, cnt + 1)
            visited[ny][nx] = cnt + 1
            q.append((ny, nx, cnt + 1))

    if tmp_virus == virus_cnt:
        time = min(time, max_time)
        return
    return




MAP = [list(map(int, input().split())) for _ in range(n)]
virus_cnt = 0
hospital_cord = []
for y in range(n):
    for x in range(n):
        if MAP[y][x] == 0:
            virus_cnt += 1
        elif MAP[y][x] == 2:
            hospital_cord.append((y, x))

l = len(hospital_cord)
tmp = [i for i in range(l)]
COMB = []
combinations([], -1)
time = 10 ** 6
for tmp in COMB:
    solve(tmp)
if virus_cnt == 0:
    print(0)
    exit(0)
print(-1 if time == 10 ** 6 else time)