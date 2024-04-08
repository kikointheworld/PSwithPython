# 21:27

import sys
from collections import deque
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def get_inputs():
    def make_factory():
        cnt = n // m
        for i in range(m):
            for j in range(cnt):
                containers[i +
                           1].append((ids[i * cnt + j], weights[i * cnt + j]))
                id_dict[ids[i * cnt + j]] = i + 1
        return

    def make_id_dict():
        for i in range(n):
            id_dict[ids[i]] = 0

    q_value = int(input())
    inputs = list(map(int, input().split()))
    n, m = inputs[1], inputs[2]
    ids, weights = inputs[3:3 + n], inputs[3 + n:]

    # 컨테이너의 갯수는 1, m  까지 m 개
    containers = [deque() for _ in range(m + 1)]
    is_container_valid = [0] + [1] * (m)

    # key = id, value = [무게, 어느컨테이너]
    id_dict = defaultdict()
    make_id_dict()
    make_factory()

    return q_value, n, m, ids, weights, containers, is_container_valid, id_dict


def hacha(w_max):
    ans = 0
    for now_container_index in range(1, m + 1):
        if not is_container_valid[now_container_index]:
            continue
        now_container = containers[now_container_index]
        if not now_container:
            continue
        while (True):
            now_id, now_weight = now_container.popleft()
            if id_dict[now_id] == -1:
                ghost_packages[now_container_index] -= 1
                continue

            if now_weight <= w_max:
                ans += now_weight
                id_dict[now_id] = -1
            else:
                now_container.append((now_id, now_weight))
            break
    print(ans)
    return


def package_delete(r_id):

    # 그러한 상자가 없으면 -1 출력
    if r_id not in id_dict:
        print(-1)
        return
    if id_dict[r_id] == -1:
        print(-1)
        return
    belt_num = id_dict[r_id]
    id_dict[r_id] = -1
    ghost_packages[belt_num] += 1
    print(r_id)

    # q = containers[belt_num]
    # l = len(q)
    # for i in range(l):
    #     now_id, now_weight = q.popleft()
    #     if now_id == r_id:
    #         continue
    #     q.append((now_id, now_weight))
    # id_dict[r_id] = -1
    return


def check_package(f_id):

    # 그러한 상자가 없으면 -1 출력
    if f_id not in id_dict:
        print(-1)
        return
    if id_dict[f_id] == -1:
        print(-1)
        return
    belt_num = id_dict[f_id]
    q = containers[belt_num]

    while (True):
        now_id, now_weight = q.popleft()
        if id_dict[now_id] == -1:
            ghost_packages[belt_num] -= 1
            continue
        if now_id == f_id:
            q.appendleft((now_id, now_weight))
            break
        else:
            q.append((now_id, now_weight))
    print(belt_num)
    return


def belt_broken(b_num):

    # 이미 고장나있을 경우
    if not is_container_valid[b_num]:
        print(-1)
        return
    is_container_valid[b_num] = 0
    broke_belt = containers[b_num]
    now_b_num = b_num
    # 이론상 m - 1개를 체크해야함.
    for _ in range(1, m):
        now_b_num += 1
        if now_b_num == m + 1:
            now_b_num = 1
        if not is_container_valid[now_b_num]:
            continue

        # 그렇지 않다면 다 옮겨줘야지.
        new_container = containers[now_b_num]
        while (broke_belt):
            now_id, now_weight = broke_belt.popleft()
            if id_dict[now_id] == -1:
                ghost_packages[b_num] -= 1
                continue
            new_container.append((now_id, now_weight))
            id_dict[now_id] = now_b_num

    print(b_num)

    return


q_value, n, m, ids, weights, containers, is_container_valid, id_dict = get_inputs()
ghost_packages = [0] * (m + 1)
for _ in range(1, q_value):
    order, value = map(int, input().split())
    if order == 200:
        hacha(value)
    elif order == 300:
        package_delete(value)
    elif order == 400:
        check_package(value)
    else:
        belt_broken(value)
