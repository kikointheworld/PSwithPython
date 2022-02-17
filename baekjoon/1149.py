'''
https://www.acmicpc.net/problem/1149
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
import math
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
d=[]

for i in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))


for i in range(1, n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + d[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + d[i][1]
    d[i][2] = min(d[i-1][1], d[i-1][0]) + d[i][2]

print(min(d[n-1][0], d[n-1][1], d[n-1][2]))

