# 00:21

import sys
from collections import deque
from itertools import combinations


def getInputs():
    n = int(input())
    scores = list(map(int, input().split()))
    graph = []
    for _ in range(n):
        tmp_list = list(map(int, input().split()))
        for i in range(tmp_list[0]):
            tmp_list[i + 1] -= 1
        graph.append(tmp_list[1:])

    return n, graph, scores


def input():
    return sys.stdin.readline().rstrip()


def solve(a_team):
    global ans
    visited = [0] * n
    q = deque()
    q.append(a_team[-1])
    visited[a_team[-1]] = 1

    len_a = len(a_team)
    cnt = 1

    while (q):
        now = q.popleft()
        for new in graph[now]:
            if new in a_team and not visited[new]:
                visited[new] = 1
                cnt += 1
                q.append(new)

    if len_a != cnt:
        return

    now = -1
    for i in range(n):
        if i not in a_team:
            now = i
            break
    if now == -1:
        print("debug")
        return

    q = deque()
    q.append(now)
    visited[now] = 1
    cnt += 1
    while (q):
        now = q.popleft()
        for new in graph[now]:
            if new not in a_team and not visited[new]:
                visited[new] = 1
                cnt += 1
                q.append(new)

    if cnt == n:
        tmp = 0
        for i in a_team:
            tmp += scores[i]
        ans = min(ans, abs(scoresSum - 2 * tmp))

    return


n, graph, scores = getInputs()
ans = 1000000
scoresSum = sum(scores)

candidates = [i for i in range(n)]

for i in range(1, n // 2 + 1):
    for new_list in combinations(candidates, i):
        solve(list(new_list))


print(-1 if ans == 1000000 else ans)
