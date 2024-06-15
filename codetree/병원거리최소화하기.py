# 14:25

import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


def dis(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


n, m = map(int, input().split())

# MAP = []
humans = []
hospitals = []

for y in range(n):
    tmp = list(map(int, input().split()))
    for x in range(n):
        if tmp[x] == 1:
            humans.append((y, x))
        if tmp[x] == 2:
            hospitals.append((y, x))
    # MAP.append(tmp)


ans = 10 ** 8
for hos_list in combinations(hospitals, m):
    tmp_ans = 0
    for h_y, h_x in humans:
        tmp_dis = 10 ** 7
        for hos_y, hos_x in hos_list:
            tmp_dis = min(tmp_dis, dis(h_y, hos_y, h_x, hos_x))
        tmp_ans += tmp_dis
    ans = min(ans, tmp_ans)
print(ans)
