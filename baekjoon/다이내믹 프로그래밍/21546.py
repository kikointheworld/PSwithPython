'''
https://www.acmicpc.net/problem/2156
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
import math
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

stair = [0 for i in range(10001)]
d = [0 for i in range(10001)]

for i in range(n):
    stair[i] = int(sys.stdin.readline())

d[0] = stair[0]
d[1] = stair[0] + stair[1]
d[2] = max(stair[1] + stair[2], stair[0] + stair[2], d[1])

for i in range(3, n):
    d[i] = max(d[i-3] + stair[i - 1] + stair[i], d[i-1],d[i-2] + stair[i])

print(max(d[n-1], d[n-2]))
