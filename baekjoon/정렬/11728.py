'''
https://www.acmicpc.net/problem/11728
'''

import sys

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


n, m = map(int,sys.stdin.readline().split())

list1 = (list(map(int, sys.stdin.readline().split())))

list2 = (list(map(int, sys.stdin.readline().split())))

list1 += list2

list1.sort()
for i in list1:
    print(i, end = ' ')
