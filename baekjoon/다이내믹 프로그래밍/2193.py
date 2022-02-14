'''
https://www.acmicpc.net/problem/2193
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
import math
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())

d = [0] * 100
d[0] = 0
d[1] = 1
d[2] = 1
for i in range(3, 100):
    d[i] = d[i-1]+d[i-2]
print(d[n])
