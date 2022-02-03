'''
https://www.acmicpc.net/problem/2752
'''

import sys

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())

n, m, k = map(int,sys.stdin.readline().split())

list1 = [n, m, k]
list1.sort()

for i in range(3):
    print(list1[i], end = " ")
