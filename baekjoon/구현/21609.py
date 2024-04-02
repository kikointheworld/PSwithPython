# 15:24 - 16:05

import sys
from collections import deque
import heapq as hq

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 0 <= y < n and 0 <= x < n


# 검은색 블록 -1, 무지개 블록 0, 일반 블록 1~M

# todo : 크기가 가장 큰 블록 그룹 찾기
# 블록 그룹이 존재하지 않는 다면, 멈춘다.
def find_block_group(round):
    global ans
    group_hq = []
    for y in range(n):
        for x in range(n):
            # 기준 블록 찾기
            # 방문했거나,.. 무지개, 검은 블록은 기준 블록이 될 수 없음.
            if visited[y][x] == round or MAP[y][x] <= 0:
                continue
            # y,x가 기준 블록
            now_color = MAP[y][x]
            visited[y][x] = round
            cnt = 1  # 블록 갯수들.
            rainbow_cnt = 0
            q = deque()
            q.append((y, x))
            candidates_list = []
            candidates_list.append((y, x))
            rainbow_list = []
            while (q):
                now_y, now_x = q.popleft()

                for dy, dx in moves:
                    ny, nx = now_y + dy, now_x + dx
                    # 범위 벗어남.
                    if not in_map(ny, nx):
                        continue
                    if visited[ny][nx] == round or MAP[ny][nx] == -1:
                        continue
                    if MAP[ny][nx] == 0 or MAP[ny][nx] == now_color:
                        if (ny, nx) in rainbow_list:
                            continue
                        candidates_list.append((ny, nx))
                        cnt += 1
                        q.append((ny, nx))
                        if MAP[ny][nx] == 0:
                            rainbow_cnt += 1
                            rainbow_list.append((ny, nx))
                        else:
                            visited[ny][nx] = round
            # 1개 이하는 될 수 없다
            if cnt == 1:
                continue
            hq.heappush(
                group_hq, (-cnt, -rainbow_cnt, -y, -x, candidates_list))
    if len(group_hq) == 0:
        return False
    cnt, rainbow_cnt, y, x, candidates_list = hq.heappop(group_hq)
    ans += cnt ** 2
    # 그룹 제거
    remove_group(candidates_list)

    # 중력 작용
    gravity()
    # 격자가 90도 반시계 방향으로 회전
    rotate()
    # 중력 작용
    gravity()

    return True


def rotate():
    tmp = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            tmp[y][x] = MAP[x][n - 1 - y]

    for y in range(n):
        for x in range(n):
            MAP[y][x] = tmp[y][x]

    return


def remove_group(candidates_list):
    for y, x in candidates_list:
        MAP[y][x] = -2
    return


def gravity():
    for x in range(n):
        for y in range(n - 2, -1, -1):
            if MAP[y][x] == -1 or MAP[y][x] == -2:
                continue
            now_y, now_x = y, x
            while (True):
                # 이미 맨 밑이거나 중력이 작용할 수 없으면 break
                if now_y + 1 == n or MAP[now_y+1][x] != -2:
                    break
                # 만약 중력 작용할 수 있으면 swap
                if MAP[now_y + 1][x] == -2:
                    MAP[now_y+1][x], MAP[now_y][x] = MAP[now_y][x], MAP[now_y+1][x]
                now_y += 1
    return


n, m = map(int, input().split())
ans = 0
MAP = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
round = 1
while (True):
    if not find_block_group(round):
        break
    round += 1
print(ans)
