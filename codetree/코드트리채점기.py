# 23:34

import sys
import heapq as hq
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

def set_tester(n, u0):
    waitingQueue = []
    testerQueue = [i for i in range(1, n + 1)]

    domain, id = map(str, u0.split('/'))
    # domain_to_id_list_dict = defaultdict(lambda : None)
    # id = int(id)

    # 이건 무조건 채점이 되면 이 아이디가 없어져야하는데..
    waitingQueue_dict = defaultdict(lambda : None)
    waitingQueue_dict[u0] = 1
    # domain_to_id_list_dict[domain] = [id]

    # 우선순위 번호가 작을수록, 시간이 빠를 수록, 그리고 도메인을 알아야 한다.
    hq.heappush(waitingQueue, (1, 0, u0))
    judging_list = [0] * (n + 1)

    # id는 도메인, 첫번째는 채점시작시간, 마지막은 gap
    history = defaultdict(lambda :None)
    now_testing_domain = defaultdict(lambda: None)

    return waitingQueue, testerQueue, waitingQueue_dict, judging_list, history, now_testing_domain

def require_test(t, p, u):
    global waitingQueue_length
    # u와 정확히 일치하는 url이 존재하면 큐에 추가하면 안됨.
    if u in waitingQueue_dict:
        return
    waitingQueue_dict[u] = 1
    # domain, id = map(str, u.split('/'))
    hq.heappush(waitingQueue, (p, t, u))
    waitingQueue_length += 1
    return

def try_test(t):
    global waitingQueue, waitingQueue_length
    q = []

    if not testerQueue:
        return

    flag = False
    while(waitingQueue):
        now_p, now_t, now_u = hq.heappop(waitingQueue)
        now_domain, id = map(str, now_u.split('/'))

        if now_domain in now_testing_domain:
            q.append((now_p, now_t, now_u))
            continue

            # if t < start + 3 * gap:
        if now_domain in history and t < history[now_domain][0] + 3 * history[now_domain][1]:
            q.append((now_p, now_t, now_u))
            continue
        flag = True
        break

    # 채점대기 큐 원상복구
    waitingQueue = q + waitingQueue

    # 채점을 할게 없다.
    if not flag:
        return

    # 채점 시작
    now_tester = hq.heappop(testerQueue)
    judging_list[now_tester] = (t, now_domain)
    now_testing_domain[now_domain] = 1
    waitingQueue_dict.pop(now_u)
    waitingQueue_length -= 1
    return

def terminate_test(t, J_id):
    # 만약 J_id  번 채점기가 진행하던 채점이 없었다면 이 명령은 무시됩니다.
    if judging_list[J_id] == 0:
        return

    start, domain = judging_list[J_id]

    # 다시 쉬는 상태.
    judging_list[J_id] = 0
    hq.heappush(testerQueue, J_id)

    # history에 추가
    history[domain] = (start, t - start)

    # now_testing_domain 에 삭제해줌.
    now_testing_domain.pop(domain)


    return

def query_waitingQueue(t):
    print(waitingQueue_length)
    return

# 채점이 진행되기만 한다면 일단 도메인만 중요함.
# 대기큐에는 근데 id 도 필요함. 단, 채점 대기 큐에 있는 task 중 정확히 u와 일치하는 url이 단 하나라도 존재한다면 큐에 추가하지 않고 넘어갑니다.
Q = int(input())
inputs = list(map(str, input().split()))
waitingQueue, testerQueue, waitingQueue_dict, judging_list, history, now_testing_domain = set_tester(int(inputs[1]), inputs[2])
waitingQueue_length = 1
# print(waitingQueue)
# print(testerQueue)
# print(waitingQueue_dict)

for _ in range(1, Q):
    inputs = list(map(str, input().split()))
    order = inputs[0]
    if order == '200':
        require_test(int(inputs[1]), int(inputs[2]), inputs[3])
    elif order == '300':
        try_test(int(inputs[1]))
    elif order == '400':
        terminate_test(int(inputs[1]), int(inputs[2]))
    elif order == '500':
        query_waitingQueue(int(inputs[1]))
    #
    # print("waitingQueue", waitingQueue)
    # print("testerQueue", testerQueue)
    # print("waitingQueue_Dict")