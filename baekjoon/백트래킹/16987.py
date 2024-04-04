# 17:30

import sys


def input():
    return sys.stdin.readline().rstrip()


def get_ans():
    tmp = 0
    for dy, dx in egg_info:
        if dy == -1 or dx == -1:
            tmp += 1
    return tmp


def backtracking(now, egg_info):
    global ans
    main_N, main_M = egg_info[now]

    if now >= n - 1:
        ans = max(ans, get_ans())
        return
    if main_N == -1 and main_M == -1:
        # 3번 과정 진행
        backtracking(now + 1, egg_info)
        return
    flag = False
    for i in range(now + 1, n):
        now_N, now_M = egg_info[i]
        if now_N != -1:
            flag = True
            break
    if not flag:
        # 3번 과정 진행
        backtracking(now + 1, egg_info)
        return

    for i in range(now + 1, n):
        now_N, now_M = egg_info[i]

        # 이미 깨진 계란은 못건든다.
        if now_N == -1 and now_M == -1:
            continue

        # 그렇지 않다면 쳐야겠지..?
        main_left_N = main_N - now_M
        now_left_N = now_N - main_M
        if main_left_N <= 0:
            continue
        if main_left_N > 0 and now_left_N > 0:
            continue
        if main_left_N <= 0:
            egg_info[now] = (-1, -1)
        else:
            egg_info[now] = (main_left_N, main_M)

        if now_left_N <= 0:
            egg_info[i] = (-1, -1)
        else:
            egg_info[i] = (now_left_N, now_M)
        backtracking(now + 1, egg_info)
        egg_info[now] = (main_N, main_M)
        egg_info[i] = (now_N, now_M)

    return


n = int(input())
ans = 0
egg_info = []
for i in range(n):
    nagu, muge = map(int, input().split())
    egg_info.append((nagu, muge))

backtracking(0, egg_info)
print(ans)
