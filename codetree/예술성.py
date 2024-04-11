# 21:24
from collections import deque

moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def in_map(y, x):
    return 0 <= y < n and 0 <= x < n

def make_group():
    visited = [[0] * n for _ in range(n)]
    now_group_num = 0
    group_cnt = [0]
    group_num = [0]
    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                continue
            now_value = MAP[y][x]
            now_group_num += 1
            cnt = 1
            visited[y][x] = now_group_num
            q = deque()
            q.append((y, x))

            while(q):
                now_y, now_x = q.popleft()
                for dy, dx in moves:
                    ny, nx = now_y + dy, now_x + dx
                    if not in_map(ny, nx):
                        continue
                    if visited[ny][nx]:
                        continue
                    if MAP[ny][nx] == now_value:
                        cnt += 1
                        visited[ny][nx] = now_group_num
                        q.append((ny, nx))
            group_cnt.append(cnt)
            group_num.append(now_value)
    return visited, group_cnt, group_num


def calculate_art_point():
    tmp = 0
    group_l = len(group_cnt) - 1

    visited = [[0] * n for _ in range(n)]

    sides_list = [[0] * (group_l + 1) for _ in range(group_l + 1)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while(q):
        y, x = q.popleft()
        now_group = group_map[y][x]
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if not in_map(ny,nx):
                continue
            new_group = group_map[ny][nx]
            if visited[ny][nx]:
                if now_group != new_group:
                    sides_list[now_group][new_group] += 1
                    sides_list[new_group][now_group] += 1
                continue
            q.append((ny, nx))
            visited[ny][nx] = 1
            if now_group != new_group:
                sides_list[now_group][new_group] += 1
                sides_list[new_group][now_group] += 1
    for i in range(1, group_l):
        for j in range(i + 1, group_l + 1):

            tmp += (group_cnt[i] + group_cnt[j]) * (sides_list[i][j] // 2) * group_num[i] * group_num[j]
    return tmp

def rotate_90(n, start_y, start_x):
    tmp = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            tmp[x][n - 1 - y] = MAP[y + start_y][x + start_x]

    for y in range(n):
        for x in range(n):
            MAP[start_y + y][start_x + x] = tmp[y][x]

    return

def rotate_minus_90(center):
    tmp = MAP[center][center + 1:]

    for i in range(center):
        tmp[i], MAP[center - 1 - i][center] = MAP[center - 1 - i][center], tmp[i]
    for i in range(center):
        tmp[i], MAP[center][center - 1 - i] = MAP[center][center - 1 - i], tmp[i]
    for i in range(center):
        tmp[i], MAP[center + 1 + i][center] = MAP[center + 1 + i][center], tmp[i]
    for i in range(center):
        tmp[i], MAP[center][center + 1 + i] = MAP[center][center + 1 + i], tmp[i]


    return

def rotate_map():
    center = n // 2
    box_n = n // 2

    # 십자모양과
    rotate_minus_90(center)

    # 나머지 네모들
    rotate_90(box_n, 0, 0)
    rotate_90(box_n, 0, center + 1)
    rotate_90(box_n, center + 1, 0)
    rotate_90(box_n, center + 1, center + 1)

    return

n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]
group_map, group_cnt, group_num = make_group()
ans = calculate_art_point()
rotate_map()
group_map, group_cnt, group_num = make_group()
ans += calculate_art_point()
rotate_map()
group_map, group_cnt, group_num = make_group()
ans += calculate_art_point()
rotate_map()
group_map, group_cnt, group_num = make_group()
ans += calculate_art_point()
print(ans)