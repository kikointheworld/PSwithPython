'''
https://www.acmicpc.net/problem/11727
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
import math
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

d = [0] * 1001

d[0] = 0
d[1] = 1
d[2] = 3
d[3] = 5

for i in range(4, 1001):
    d[i] = d[i-1] + 2 * d[i-2]
    d[i] %= 10007


print(d[n])
