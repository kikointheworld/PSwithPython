# 00:52 02:31

import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

def remove_package_in_dict(id):
    prev.pop(id)
    next.pop(id)
    belts.pop(id)
    weights.pop(id)
    return

def build_factory(inputs):
    n, m = inputs[1], inputs[2]
    belts = defaultdict(lambda : 0)
    isBeltsAvailable = [False] + [True] * (m)
    weights = defaultdict(lambda : 0)

    next = defaultdict(lambda : 0)
    prev = defaultdict(lambda : 0)

    size = n // m
    id_list = inputs[3:n + 3]
    weight_list = inputs[n + 3:]

    front = [0] * (m + 1)
    end = [0] * (m + 1)

    # set next, prev, belts, weights
    for i in range(n):

        j = i // size
        tmp = i % size
        id, weight = id_list[i], weight_list[i]
        belts[id] = j + 1
        weights[id] = weight
        if tmp != 0:
            prev[id] = id_list[i - 1]
        else:
            prev[id] = 0
            front[j + 1] = id
        if tmp != size - 1:
            next[id] = id_list[i + 1]
        else:
            next[id] = 0
            end[j + 1] = id

    return n, m, belts, isBeltsAvailable, weights, next, prev, front, end

def package_down(w_max):
    tmp = 0
    for now_belt in range(1, m + 1):
        if not isBeltsAvailable[now_belt]:
            continue
        now_id = front[now_belt]
        now_weight = weights[now_id]
        # 무게가 w_max 이하라면 하차를 진행한다.
        if now_weight <= w_max:
            tmp += now_weight
            now_next = next[now_id]
            front[now_belt] = now_next
            prev[now_next] = 0

            remove_package_in_dict(now_id)

        else:
            now_next = next[now_id]
            next[end[now_belt]] = now_id
            front[now_belt] = now_next
            prev[now_next] = 0
            prev[now_id] = end[now_belt]
            next[now_id] = 0
            end[now_belt] = now_id

    print(tmp)
    return

def delete_package(r_id):
    if r_id not in belts:
        print(-1)
        return
    now_belt = belts[r_id]
    now_next = next[r_id]
    now_prev = prev[r_id]

    # 뒤가 없는 애

    # 둘다없는애..?
    if now_next == 0:
        if now_prev == 0:
            front[now_belt] = 0
            end[now_belt] = 0
        else:
            next[now_prev] = 0
            end[now_belt] = now_prev
    # 앞이 없는 애
    elif now_prev == 0:
        prev[now_next] = 0
        front[now_belt] = now_next
    else:
        next[now_prev] = now_next
        prev[now_next] = now_prev

    remove_package_in_dict(r_id)
    print(r_id)
    return

def check_package(f_id):
    if f_id not in belts:
        print(-1)
        return
    now_belt = belts[f_id]
    print(now_belt)
    now_prev = prev[f_id]
    now_next = next[f_id]
    original_front = front[now_belt]
    original_end = end[now_belt]
    # 맨 뒤에 있단 소리
    if now_next == 0:
        # 벨트에 얘밖에 없음.
        if now_prev == 0:
            front[now_belt] = f_id
            return

        prev[original_front] = f_id
        prev[f_id] = 0
        next[f_id] = original_front
        end[now_belt] = now_prev
        next[now_prev] = 0

    #  원래 맨 앞이었음.
    elif now_prev == 0:
        front[now_belt] = f_id
        return

    # 아무튼 중간
    else:
        prev[f_id] = 0
        prev[original_front] = original_end
        next[original_end] = original_front
        next[now_prev] = 0
        # prev[now_next] = now_prev
        end[now_belt] = now_prev


    front[now_belt] = f_id
    return

def break_belt(b_num):
    if not isBeltsAvailable[b_num]:
        print(-1)
        return
    new_belt = 0
    for i in range(m + 1):
        idx = 1 + ((i + b_num) % m)
        if isBeltsAvailable[idx]:
            new_belt = idx
            break
    print(b_num)
    isBeltsAvailable[b_num] = False

    # 벨트가 원래 아무도 없었을 때
    if front[b_num] == 0:
        return
    # 일단 애들 belts 모두 바꿔주기
    now = front[b_num]

    while(True):
        belts[now] = new_belt

        if next[now] == 0:
            break
        now = next[now]


    # 옮기려는 벨트가 비었을 때
    if front[new_belt] == 0:
        front[new_belt] = front[b_num]
        end[new_belt] = end[b_num]
        return
    # 안비었을때

    new_belt_end = end[new_belt]
    next[new_belt_end] = front[b_num]
    end[new_belt] = end[b_num]
    prev[front[b_num]] = new_belt_end
    return



q = int(input())
inputs = list(map(int, input().split()))
n, m, belts, isBeltsAvailable, weights, next, prev, front, end = build_factory(inputs)
# print(n, m)
# print("belts", belts, len(belts))
# print("isBeltsAvailable", isBeltsAvailable)
# print("weights", weights, len(weights))
# print("next", next)
# print("prev", prev)
#
# print(front)
# print(end)

for _ in range(1, q):
    order, value = map(int, input().split())
    if order == 200:
        package_down(value)
    elif order == 300:
        delete_package(value)
    elif order == 400:
        check_package(value)
    else:
        break_belt(value)

# print("belts", belts, len(belts))
# print("isBeltsAvailable", isBeltsAvailable)
# print("weights", weights, len(weights))
# print("next", next)
# print("prev", prev)
# print(front)
# print(end)