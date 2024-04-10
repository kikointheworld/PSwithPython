# 20:17

import sys

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def input():
    return sys.stdin.readline().rstrip()

def make_cords():
    y, x = main_y, main_x
    tmp = [(y, x - 1),
           (y + 1, x - 1),
           (y + 1, x),
           (y + 1, x + 1),
           (y, x + 1),
           (y-1, x + 1),
           (y - 1, x),
           (y - 1, x - 1)]
    if n == 3:
        return tmp

    5 - 1, 7 - 2, 9 - 3
    cycle = (n - 3) // 2
    l = 4
    y = main_y - 1
    x = main_x - 1
    for _ in range(cycle):
        x -= 1
        tmp.append((y, x))
        for i in range(l - 1):
            y += 1
            tmp.append((y, x))
        for i in range(l):
            x += 1
            tmp.append((y, x))
        for i in range(l):
            y -= 1
            tmp.append((y, x))
        for i in range(l):
            x -= 1
            tmp.append((y, x))

        l += 2

    return tmp

def attack(dir, p):
    global ans
    dy, dx = moves[dir]
    for i in range(1, p + 1):
        ans += MAP[main_y + i * dy][main_x + i * dx]
        MAP[main_y + i * dy][main_x + i * dx] = 0
    return


# todo: 개선의 여지가 있음.
def filling2():
    for i in range(cords_l):
        now_y, now_x = cords[i]
        if MAP[now_y][now_x] == 0:
            for j in range(i + 1, cords_l):
                y, x = cords[j]
                if MAP[y][x] == 0:
                    continue
                else:
                    MAP[now_y][now_x], MAP[y][x] = MAP[y][x], MAP[now_y][now_x]
                    break
    return

def filling():
    now, next = 0, 1
    while(True):
        now_y, now_x = cords[now]
        if MAP[now_y][now_x] == 0:
            while(True):
                if next >= cords_l:
                    return
                next_y, next_x = cords[next]
                if MAP[next_y][next_x] != 0:
                    MAP[now_y][now_x], MAP[next_y][next_x] = MAP[next_y][next_x], MAP[now_y][now_x]
                    next += 1
                    break
                else:
                    next += 1
            now += 1
        else:
            now += 1
            next += 1

    return

def bomb():
    global ans
    tmp = []
    num = -1
    cnt = 0
    num_list = []
    for y, x in cords:
        new = MAP[y][x]
        if new == 0:
            break
        if num != new:
            if cnt >= 4:
                tmp.append((num, num_list))
            num = new
            cnt = 1
            num_list = [(y, x)]
            continue
        cnt += 1
        num_list.append((y, x))
    if cnt >= 4:
        tmp.append((num, num_list))

    for num, num_list in tmp:
        for y, x in num_list:
            ans += num
            MAP[y][x] = 0
    if tmp:
        return True
    else:
        return False

def duplicate():
    tmp = []
    y, x = cords[0]
    now = MAP[y][x]
    cnt = 1
    for i in range(1, cords_l):
        y, x = cords[i]
        if MAP[y][x] == 0:
            break
        if MAP[y][x] == now:
            cnt += 1
        else:
            tmp.append(cnt)
            tmp.append(now)
            now = MAP[y][x]
            cnt = 1
    tmp.append(cnt)
    tmp.append(now)
    l = min(cords_l, len(tmp))
    for i in range(l):
        y, x = cords[i]
        MAP[y][x] = tmp[i]
    return


n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
main_y, main_x = n // 2, n // 2
cords = make_cords()
cords_l = len(cords)
ans = 0
for _ in range(m):
    d, p = map(int, input().split())
    attack(d, p)
    filling()
    while(bomb()):
        filling()
    duplicate()


print(ans)