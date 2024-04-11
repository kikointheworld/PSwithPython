# 19:15

from collections import defaultdict
import sys

class Box():
    def __init__(self, belt, nxt, prv):
        self.belt = belt
        self.nxt = nxt
        self.prv = prv


def input():
    return sys.stdin.readline().rstrip()

def box_printer(box_dict):
    for key in box_dict:
        now_box = box_dict[key]
        print("now box :", key)
        print("belt:", now_box.belt)
        print("next:",  now_box.nxt)
        print("prev:",  now_box.prv)
    return
def make_factory(inputs):
    n, m = inputs[1], inputs[2]
    tmp = [[] for _ in range(n + 1)]
    for i in range(3, m + 3):
        box_id = i - 2
        tmp[inputs[i]].append(box_id)

    front = [-1] * (n + 1)
    end = [-1] * (n + 1)
    box_dict = defaultdict(lambda : None)
    box_len_list = [0] * (n + 1)

    for now_belt in range(1, n + 1):
        l = len(tmp[now_belt])
        box_len_list[now_belt] = l
        for i in range(l):
            box_id = tmp[now_belt][i]
            if i == 0:
                front[now_belt] = box_id
                prv = -1
            else:
                prv = tmp[now_belt][i - 1]
            if i == l - 1:
                end[now_belt] = box_id
                nxt = -1
            else:
                nxt = tmp[now_belt][i + 1]
            box = Box(now_belt, nxt, prv)
            box_dict[box_id] = box

    return n, m, box_dict, front, end, box_len_list
def change_allbox_belt_num(src, dst):
    now = front[src]
    while(True):
        if now == -1:
            break
        box_dict[now].belt = dst
        now = box_dict[now].nxt
    return


def move_all_box(src, dst):
    src_len, dst_len = belt_len(src), belt_len(dst)
    # 소스가 비어있다면 아무것도 옮기지 않아도 된다.
    if src_len == 0:
        print(dst_len)
        return

    # src의 마지막애는 dst의 마지막과 연동을 해주어여한다.
    if dst_len == 0:
        # 프론트와 엔드는 모두 바꿔줬다.
        # change_allbox_belt_num(src, dst) # 벨트넘버를 바꿔야한다.
        front[dst], end[dst] = front[src], end[src]
        front[src], end[src] = -1, -1

    else:
        # change_allbox_belt_num(src, dst)

        dst_front_box_id = front[dst]
        src_end_box_id = end[src]

        box_dict[dst_front_box_id].prv = src_end_box_id
        box_dict[src_end_box_id].nxt = dst_front_box_id

        front[dst] = front[src]
        front[src], end[src] = -1, -1

    box_len_list[dst] += box_len_list[src]
    box_len_list[src] = 0
    print(box_len_list[dst])
    return
def move_only_front(src, dst):
    src_len, dst_len = belt_len(src), belt_len(dst)
    if src_len == 0 and dst_len == 0:
        print(dst_len)
        return

    if src_len == 0:
        #  dst에도 한개밖에 없었을 떄
        if dst_len == 1:
            now_id = front[dst]
            now = box_dict[now_id]
            now.belt = src
            front[src], end[src] = now_id, now_id

            front[dst], end[dst] = -1, -1
            box_len_list[src] += 1
            box_len_list[dst] -= 1
            print(dst_len - 1)
            return
        # dst에 여러개있었을 때
        else:
            now_id = front[dst]
            now = box_dict[now_id]
            now.belt = src
            front[src], end[src] = now_id, now_id

            next_id = now.nxt
            now.nxt = -1
            front[dst] = next_id
            next = box_dict[next_id]
            next.prv = -1
            box_len_list[src] += 1
            box_len_list[dst] -= 1
            print(dst_len - 1)
            return

    if dst_len == 0:
        #  src에도 한개밖에 없었을 떄
        if src_len == 1:
            now_id = front[src]
            now = box_dict[now_id]
            now.belt = dst
            front[dst], end[dst] = now_id, now_id

            front[src], end[src] = -1, -1

            box_len_list[src] -= 1
            box_len_list[dst] += 1
            print(1)
            return
        # src에 여러개있었을 때
        else:
            now_id = front[src]
            now = box_dict[now_id]
            now.belt = dst
            front[dst], end[dst] = now_id, now_id

            next_id = now.nxt
            now.nxt = -1
            front[src] = next_id
            next = box_dict[next_id]
            next.prv = -1

            box_len_list[src] -= 1
            box_len_list[dst] += 1
            print(1)
            return


    src_front_id, dst_front_id = front[src], front[dst]
    src_front_box, dst_front_box = box_dict[src_front_id], box_dict[dst_front_id]
    src_second_id, dst_second_id = src_front_box.nxt, dst_front_box.nxt

    front[src], front[dst] = front[dst], front[src]
    src_front_box.belt, dst_front_box.belt = dst, src


    if src_second_id == -1 and dst_second_id == -1:
        end[src], end[dst] = end[dst], end[src]
    elif src_second_id == -1:
        dst_second_box = box_dict[dst_second_id]
        dst_second_box.prv = src_front_id

        src_front_box.nxt = dst_second_id
        dst_front_box.nxt = -1
        end[src] = dst_front_id

    elif dst_second_id == -1:
        src_second_box = box_dict[src_second_id]
        src_second_box.prv = dst_front_id

        dst_front_box.nxt = src_second_id
        src_front_box.nxt = -1
        end[dst] = src_front_id

    else:
        dst_second_box = box_dict[dst_second_id]
        src_second_box = box_dict[src_second_id]

        src_front_box.nxt = dst_second_id
        dst_front_box.nxt = src_second_id

        dst_second_box.prv = src_front_id
        src_second_box.prv = dst_front_id

    print(dst_len)
    return

def divide_box(src, dst):
    n = belt_len(src)
    dst_len = belt_len(dst)
    if n <= 1:
        print(dst_len)
        return

    cnt = n // 2

    # src먼저 바꾸자...
    first_id, last_id = front[src], -1
    now_id = first_id
    for _ in range(cnt):
        now_box = box_dict[now_id]
        now_box.belt = dst
        now_id = now_box.nxt
    front[src] = now_id

    # 라스트 애의 넥스트를 재지정해줘야한다.
    last_id = box_dict[now_id].prv
    box_dict[now_id].prv = -1

    # first_id와 last_id를 구했다. 이제 벨트에 합치자.

    dst_original_front = front[dst]
    if dst_original_front == -1:
        front[dst], end[dst] = first_id, last_id
        box_dict[last_id].nxt = -1
    else:
        front[dst] = first_id

        box_dict[dst_original_front].prv = last_id
        box_dict[last_id].nxt = dst_original_front

    box_len_list[src] -= cnt
    box_len_list[dst] += cnt
    print(box_len_list[dst])
    return

def get_box_info(p_num):
    now_box = box_dict[p_num]
    a = now_box.prv
    b = now_box.nxt
    print(a + 2 * b)
    return

def belt_len(b_num):
    return box_len_list[b_num]
    # now = front[b_num]
    # tmp = 0
    # while(True):
    #     if now == -1:
    #         break
    #     tmp += 1
    #     now = box_dict[now].nxt
    #
    # return tmp

def get_belt_info(b_num):
    a = front[b_num]
    b = end[b_num]
    c = belt_len(b_num)
    print(a + 2 * b + 3 * c)
    return

Q = int(input())

inputs = list(map(int, input().split()))
n, m, box_dict, front, end, box_len_list = make_factory(inputs)

for _ in range(1, Q):
    inputs = list(map(int, input().split()))
    order = inputs[0]
    if order == 200:
        move_all_box(inputs[1], inputs[2])
    elif order == 300:
        move_only_front(inputs[1], inputs[2])
    if order == 400:
        divide_box(inputs[1], inputs[2])
    if order == 500:
        get_box_info(inputs[1])
    if order == 600:
        get_belt_info(inputs[1])