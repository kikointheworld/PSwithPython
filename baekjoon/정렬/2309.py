'''
https://www.acmicpc.net/problem/2309
'''

import sys

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())

d = []

for _ in range(9):
    d.append(int(sys.stdin.readline()))

sum_of_nine = sum(d)

d.sort()

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if sum_of_nine - d[i] - d[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(d[k])
            exit()
