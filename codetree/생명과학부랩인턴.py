# 21:57

from itertools import permutations, combinations
import itertools
import sys
from collections import deque

moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def input():
    return sys.stdin.readline().rstrip()


def get_input():
    y, x, s, d, b = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    return y, x, s, d, b


def kill_bug(bug_id):
    bugs_alive[bug_id] = 0
    bugs_cord[bug_id] = [-1, -1]
    return


def explore():
    global ans
    for man_y in range(n):
        if MAP[man_y][man_x]:
            _, _, b, id = MAP[man_y][man_x].popleft()
            ans += b
            kill_bug(id)
            return
    return


def move_single_bug(y, x, s, d):
    dy, dx = moves[d]
    if d == 0 or d == 1:
        ny = (y + s * dy) % (2 * (n - 1))
        if ny < n:
            return ny, x, d
        else:
            ny = (2 * (n - 1)) - ny
            if d == 1:
                d = 0
            else:
                d = 1
            return ny, x, d

    if d == 3 or d == 2:
        nx = (x + s * dx) % (2 * (m - 1))
        if nx < m:
            return y, nx, d
        else:
            nx = (2 * (m - 1)) - nx
            if d == 3:
                d = 2
            else:
                d = 3
            return y, nx, d

    return


def move_bugs():
    for now_bug in range(k):
        if bugs_alive[now_bug] == 0:
            continue

        y, x = bugs_cord[now_bug][0], bugs_cord[now_bug][1]
        s, d, b, id = MAP[y][x].popleft()

        y, x, d = move_single_bug(y, x, s, d)
        MAP[y][x].append((s, d, b, id))
        bugs_cord[id] = [y, x]

    return


def bug_fight():
    for y in range(n):
        for x in range(m):
            if len(MAP[y][x]) > 1:
                s, d, b, id = MAP[y][x].popleft()
                while (MAP[y][x]):
                    ns, nd, nb, nid = MAP[y][x].popleft()
                    if nb > b:
                        kill_bug(id)
                        s, d, b, id = ns, nd, nb, nid
                    else:
                        kill_bug(nid)
                MAP[y][x].append((s, d, b, id))
    return


n, m, k = map(int, input().split())

MAP = [[deque() for _ in range(m)] for _ in range(n)]
bugs_cord = [[-1, -1] for _ in range(k)]
bugs_alive = [1] * k
for bugs_id in range(k):
    y, x, s, d, b = get_input()
    MAP[y][x].append((s, d, b, bugs_id))
    bugs_cord[bugs_id] = [y, x]

ans = 0
for man_x in range(m):
    # 1번 과정
    explore()
    # 곰팡이 이동 과정
    move_bugs()
    # 곰팡이가 다 잡아먹음
    bug_fight()
    # print()
    # for i in MAP:
    #     print(i)
    # print("bugs_alive", bugs_alive)
    # print("bugs_cord", bugs_cord)
    # print()
print(ans)
# 5 6 5
# 2 1 5 3 3
# 2 5 5 2 2
# 3 2 0 3 1
# 5 1 1 4 5
# 5 3 4 1 4
itertools.permutations()


def list_to_int(x):
    ans = ''
    for i in x:
        ans += str(i)
    return int(ans)


n = int(input())
n -= 6

tmp_list = [1, 1, 1, 2, 2, 2]

ans_set = set()

p_list = permutations(tmp_list, 6)


for j in p_list:
    ans_set.add(list_to_int(j))

for i in list(ans_set).sort():
    print(i)
