'''
https://www.acmicpc.net/problem/7568
'''

n = int(input())

ans_list = []

for _ in range(n):
    weight, height = map(int, input().split())

    ans_list.append([weight, height])


for i in ans_list:
    rank = 1

    for j in ans_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")
