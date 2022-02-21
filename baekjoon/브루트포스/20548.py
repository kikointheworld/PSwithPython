'''
https://www.acmicpc.net/problem/20548
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys

c = int(sys.stdin.readline()) 

tmp = 1 # 7로 나눌때 마다 3씩 곱해져서 더해짐
level = 0 # 단계
while c > 0:
    level += (c % 7) * tmp
    tmp *= 3
    c //= 7
print(level)
