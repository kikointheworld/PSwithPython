# 15:57

import sys
from itertools import combinations, permutations



def input():
    return sys.stdin.readline().rstrip()

def rotate(graph):
    n = 4
    tmp = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            tmp[x][n - 1 - y] = graph[y][x]
    return tmp

def get_ans(GAMA):
    tmp_dict = dict()
    tmp_dict["R"] = 0
    tmp_dict["B"] = 0
    tmp_dict["G"] = 0
    tmp_dict["Y"] = 0
    tmp_dict["W"] = 0

    # r, b, g, y = 0
    for y in range(5):
        for x in range(5):
            tmp_dict[GAMA[1][y][x]] += GAMA[0][y][x]


    return 7 * tmp_dict["R"] + 5 * tmp_dict["B"] + 3 * tmp_dict["G"] + 2 * tmp_dict["Y"]
def cal(a):
    if a < 0:
        return 0
    if a >= 9:
        return 9
    return a

def use_zeryo(GAMA, now_power_and_color, start_y, start_x):

    power = now_power_and_color[0]
    color = now_power_and_color[1]

    gama_power = GAMA[0]
    gama_color = GAMA[1]

    for y in range(4):
        for x in range(4):
            gama_power[start_y + y][start_x + x] = cal(gama_power[start_y + y][start_x + x] + power[y][x])
            if color[y][x] == "W":
                continue
            gama_color[start_y + y][start_x + x] = color[y][x]

    return



n = int(input())
zeryo_info = [[] for _  in range(n)]
for i in range(n):
    power = [list(map(int, input().split())) for _ in range(4)]
    color = [list(map(str, input().split())) for _ in range(4)]

    rotate_power_90 = rotate(power)
    rotate_color_90 = rotate(color)

    rotate_power_180 = rotate(rotate_power_90)
    rotate_color_180 = rotate(rotate_color_90)

    rotate_power_270 = rotate(rotate_power_180)
    rotate_color_270 = rotate(rotate_color_180)

    zeryo_info[i].append([power, color])
    zeryo_info[i].append([rotate_power_90, rotate_color_90])
    zeryo_info[i].append([rotate_power_180, rotate_color_180])
    zeryo_info[i].append([rotate_power_270, rotate_color_270])


ans = 0
# 주어진 재료 3개를 고르자. 순서를 고려해서 permutations 이용

permutations_list = list(permutations([i for i in range(0, n)], 3))

rc_list = list(permutations([(0, 0),(0, 1),(1, 0),(1, 1)], 3))


for one, two, three in permutations_list:

    # 에이씨발
    for one_dir in range(4):
        for two_dir in range(4):
            for three_dir in range(4):
                now_one = zeryo_info[one][one_dir]
                now_two = zeryo_info[two][two_dir]
                now_three = zeryo_info[three][three_dir]
                for now_start in rc_list:
                    one_y, one_x = now_start[0]
                    two_y, two_x = now_start[1]
                    three_y, three_x = now_start[2]

                    GAMA = [[[0] * 5 for _ in range(5)], [["W", "W", "W", "W", "W"] for _ in range(5)]]

                    use_zeryo(GAMA, now_one, one_y, one_x)
                    use_zeryo(GAMA, now_two, two_y, two_x)
                    use_zeryo(GAMA, now_three, three_y, three_x)

                    ans = max(ans, get_ans(GAMA))

print(ans)