# 20:25 20:44

import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def moving_walk_rotate():
    walk_q.appendleft(walk_q.pop())
    # 사람이 같이 움직이면 이는 내구도에 영향 x

    # 마지막칸에 사람있었으면 내려줘야함.
    human_q.appendleft(0)
    human_q.pop()
    return


def human_move():
    # 마지막 칸에 사람 있으면 그냥 내리면 됨.
    if human_q[-1] == 1:
        human_q[-1] = 0

    for now in range(n - 2, -1, -1):
        if human_q[now] == 0:
            continue

        if walk_q[now + 1] == 0:
            continue

        if human_q[now + 1] == 1:
            continue

        human_q[now] = 0
        human_q[now + 1] = 1
        walk_q[now + 1] -= 1

    # 마지막 칸에 사람 있으면 그냥 내리면 됨.
    if human_q[-1] == 1:
        human_q[-1] = 0
    return


def add_human():
    # 만약 사람 올라갈 수 있으면 올라가고, 올라갈 시 내구도 즉시 감소
    if walk_q[0] != 0 and human_q[0] != 1:
        human_q[0] = 1
        walk_q[0] -= 1
    return


def is_safety():
    tmp = 0
    for i in walk_q:
        if i == 0:
            tmp += 1
        if tmp >= k:
            return False
    return True


n, k = map(int, input().split())
walk_q = deque(list(map(int, input().split())))
human_q = deque([0] * n)
ans = 0

while (True):
    ans += 1
    moving_walk_rotate()
    human_move()
    add_human()
    if not is_safety():
        break
print(ans)