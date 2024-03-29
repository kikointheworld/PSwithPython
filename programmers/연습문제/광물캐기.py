# 14:51 15:12
from collections import deque


def solution(picks, minerals):
    dia, iron, stone = picks
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]
    n = len(minerals) // 5
    tmp_list = []

    for i in range(n):
        tmp = 0
        for j in range(5):
            if minerals[j + i * 5] == "diamond":
                tmp += 25
            elif minerals[j + i * 5] == "iron":
                tmp += 5
            else:
                tmp += 1
        tmp_list.append([tmp, minerals[i * 5: i * 5 + 5]])
    tmp = 0
    if len(minerals) % 5 != 0:
        for j in range(5 * n, len(minerals)):
            if minerals[j] == "diamond":
                tmp += 25
            elif minerals[j] == "iron":
                tmp += 5
            else:
                tmp += 1
        tmp_list.append([tmp, minerals[n * 5: len(minerals)]])
    tmp_list.sort(reverse=True)

    ans = 0
    for new_list in tmp_list:
        target = new_list[1]

        now = -1
        for i in range(3):
            if picks[i] != 0:
                picks[i] -= 1
                now = i
                break
        if now == -1:
            return ans

        if now == 0:
            ans += len(target)

        elif now == 1:
            for t in target:
                if t == "diamond":
                    ans += 5
                else:
                    ans += 1
        else:
            for t in target:
                if t == 'diamond':
                    ans += 25
                elif t == 'iron':
                    ans += 5
                else:
                    ans += 1

    return ans
