'''
https://www.acmicpc.net/problem/1932
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
import math
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

d = [[0]]

for _ in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n + 1):
    for j in range(i):
        if j == 0:
            d[i][j] += d[i - 1][0]
        elif j == i -1:
            d[i][j] += d[i - 1][j - 1]
        else:
            if d[i - 1][j] > d[i-1][j-1]:
                d[i][j] += d[i - 1][j]
            else:
                d[i][j] += d[i-1][j-1]


print(max(d[n]))
