'''
https://www.acmicpc.net/problem/11004
'''

import sys

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())

n, k = map(int,sys.stdin.readline().split())

list1 = list(map(int, sys.stdin.readline().split()))

list1.sort()

print(list1[k - 1])
