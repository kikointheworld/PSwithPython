'''
https://www.acmicpc.net/problem/1699
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
import math
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

d = [0 for i in range(n + 1)]
s = [i ** 2 for i in range(1, 320)]

for i in range(1, n + 1):
    tmp = []
    for j in s:
        if j > i:
            break
        tmp.append(d[i - j] + 1)
    d[i] = min(tmp)

print(d[n])
