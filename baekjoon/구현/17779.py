# 15:21

import sys


def input():
    return sys.stdin.readline().rstrip()


def in_map(y, x):
    return 1 <= y <= n and 1 <= x <= n


def getInput():
    tmp_n = int(input())
    tmp_list = [[0] * (tmp_n + 1)]
    for _ in range(tmp_n):
        tmp_list.append([0] + list(map(int, input().split())))
    tmp_sum = 0
    for i in tmp_list:
        tmp_sum += sum(i)

    return tmp_n, tmp_list, tmp_sum


def sumPopulation(r_1, r_2, c_1, c_2, cnt):
    tmp = 0
    for r in range(r_1, r_2):
        for c in range(c_1, c_2):
            tmp += MAP[r][c]
            if graph[r][c] != 0:
                print("debuh")
            graph[r][c] = cnt

    return tmp


def solve(x, y, d1, d2):
    global ans
    mini, maxi = 10 ** 7, 0

    one = sumPopulation(1, x + d1, 1, y + 1, 1)
    mini, maxi = min(mini, one), max(maxi, one)

    two = sumPopulation(1, x + d2 + 1, y + 1, n + 1, 2)
    mini, maxi = min(mini, two), max(maxi, two)

    three = sumPopulation(x + d1, n + 1, 1, y - d1 + d2, 3)
    mini, maxi = min(mini, three), max(maxi, three)

    four = sumPopulation(x + d2 + 1, n + 1, y - d1 + d2, n + 1, 4)
    mini, maxi = min(mini, four), max(maxi, four)

    five = sumi - (one + two + three + four)
    mini, maxi = min(mini, five), max(maxi, five)

    ans = min(ans, maxi - mini)
    # print(one, two, three, four, five)

    return


n, MAP, sumi = getInput()
graph = [[0] * (n + 1) for _ in range(n + 1)]
ans = 10 ** 7
candidates = 0
candidates2 = 0
for x in range(1, n - 1):
    for y in range(2, n):
        for d1 in range(1, n - 1):
            for d2 in range(1, n - 1):
                if 1 <= y - d1 and x + d1 + d2 <= n and y + d2 <= n:
                    solve(x, y, d1, d2)
                    candidates += 1

                    print("prinitinti")
                    for i in graph:
                        print(i)

                    print()

                # else:
                #     break
                # if x < x + d1 + d2 and x + d1 + d2 <= n:
                #     if 1 <= y - d1 and y - d1 < y and y < y + d2 and y + d2 <= n:
                #         candidates2 += 1
print(ans)
print(candidates)  # 65
print(candidates2)  # 65
