# 14:43

import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()

def get_inputs(input_parents, input_authority):
    left = [-1] * (N + 1)
    right = [-1] * (N + 1)
    isNotifiable = [True] * (N + 1)

    parents = [-1] + input_parents
    authority = [-1] + input_authority


    # 이제 left right만 수정하면 될듯.
    for i in range(1, N + 1):
        now_parent = parents[i]

        if left[now_parent] == -1:
            left[now_parent] = i
        else:
            right[now_parent] = i



    return left, right, isNotifiable, parents, authority

# isNotifiable 가 false 면 부모한테 알람을 못 보냄.

def notification_setting(c):
    isNotifiable[c] = not isNotifiable[c]

    return

def change_authority(c, power):
    authority[c] = power
    return

def change_parent(c1, c2):
    c1_original_parent = parents[c1]
    c2_original_parent = parents[c2]
    parents[c1], parents[c2] = parents[c2], parents[c1]
    # 그러면 c1, c2의 부모도 left, right바꿔줘야한다.
    if left[c1_original_parent] == c1:
        left[c1_original_parent] = c2
    else:
        right[c1_original_parent] = c2

    if left[c2_original_parent] == c2:
        left[c2_original_parent] = c1
    else:
        right[c2_original_parent] = c1



    return

def check_notifiable_chats(c):
    print(ans_nums[c])
    return

def set_ans_nums():
    ans_nums = [0] * (N + 1)
    child_list = []
    for i in range(1, N + 1):
        child_list.append((i, authority[i]))
    # print("child_list", child_list)
    child_list = deque(child_list)
    while(child_list):
        now, depth = child_list.popleft()

        now_parents = parents[now]

        ans_nums[now_parents] += 1

        if depth == 1:
            continue

        # 메인 채팅방일 경우도
        if now_parents == 0:
            continue

        child_list.append((now_parents, depth - 1))
    # print("ans_nums", ans_nums)
    return ans_nums

N, Q = map(int, input().split())

inputs = list(map(int, input().split()))

left, right, isNotifiable, parents, authority = get_inputs(inputs[1:N + 1], inputs[N + 1 : 2 * N + 1])


ans_nums = set_ans_nums()

print("left", left)
print("right", right)
print("isNotifiable", isNotifiable)
print("parents", parents)
print("authority", authority)
print("ans_nums", ans_nums)


for _ in range(1, Q):
    inputs = list(map(int, input().split()))
    order = inputs[0]

    if order == 200:
        notification_setting(inputs[1])
    elif order == 300:
        change_authority(inputs[1], inputs[2])
    elif order == 400:
        change_parent(inputs[1], inputs[2])
    if order == 500:
        check_notifiable_chats(inputs[1])

    print("NOW ORDER", order)
    print("left", left)
    print("right", right)
    print("isNotifiable", isNotifiable)
    print("parents", parents)
    print("authority", authority)
    print("ans_nums", ans_nums)