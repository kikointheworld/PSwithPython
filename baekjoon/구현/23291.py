# 1시간 13분

import sys

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def input():
    return sys.stdin.readline().rstrip()


def add_one(flours):
    l = len(flours)
    index_list = []
    tmp = 10 ** 6

    for i in range(l):
        if flours[i] < tmp:
            index_list = [i]
            tmp = flours[i]
        elif flours[i] == tmp:
            index_list.append(i)

    for i in index_list:
        flours[i] += 1
    return


def rotate(graph):
    y_len, x_len = len(graph), len(graph[0])
    tmp = [[0] * y_len for _ in range(x_len)]

    for y in range(y_len):
        for x in range(x_len):
            tmp[x][y_len - 1 - y] = graph[y][x]
    return tmp


def push_pizza(graph):
    tmp = []
    graph_l = len(graph)
    for y in range(graph_l):
        L = len(graph[y])
        for x in range(L):
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if 0 <= ny < graph_l and 0 <= nx < len(graph[ny]):
                    d = abs(graph[y][x] - graph[ny][nx]) // 5
                    if d == 0:
                        continue
                    if graph[y][x] > graph[ny][nx]:
                        tmp.append((y, x, -(d/2)))
                        tmp.append((ny, nx, (d/2)))
                    else:
                        tmp.append((y, x, (d/2)))
                        tmp.append((ny, nx, -(d/2)))
    for y, x, value in tmp:
        graph[y][x] += value

    ans = []
    x_len = len(graph[0])

    for x in range(x_len):
        for y in range(graph_l - 1, -1, -1):
            ans.append(graph[y][x])
    for x in range(x_len, len(graph[-1])):
        ans.append(graph[-1][x])

    return ans


def roll_and_push(flours):
    l = len(flours)
    if l == 1:
        return flours
    now_index = 1
    tmp = [[flours[0]]]
    while (True):
        tmp.append(flours[now_index:now_index + len(tmp[0])])
        now_index += len(tmp[0])
        if len(tmp) + now_index > n:
            break
        tmp = rotate(tmp)

    while (now_index < n):
        tmp[-1].append(flours[now_index])
        now_index += 1

    return push_pizza(tmp)


def half_twice_and_push(flours):
    half = n // 2
    tmp = []
    tmp.append(flours[::-1][half:])
    tmp.append(flours[half:])

    half = half // 2

    ans = []
    ans.append(tmp[1][:half][::-1])
    ans.append(tmp[0][:half][::-1])
    ans.append(tmp[0][half:])
    ans.append(tmp[1][half:])

    return push_pizza(ans)


n, k = map(int, input().split())
flours = list(map(int, input().split()))


times = 1
while (True):
    add_one(flours)
    flours = roll_and_push(flours)
    flours = half_twice_and_push(flours)

    if max(flours) - min(flours) <= k:
        break

    times += 1
print(times)
