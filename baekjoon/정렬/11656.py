'''
https://www.acmicpc.net/problem/11656
'''

import sys

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때

s = str(sys.stdin.readline().rstrip())

list1 = []

l = len(s)

for i in range(l):
    list1.append(s[i:l])
list1.sort()

for j in list1:
    print(j)
