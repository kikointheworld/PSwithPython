'''
https://www.acmicpc.net/problem/5052
'''

import sys

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    list1 = []
    for _ in range(n):
        list1.append(sys.stdin.readline().rstrip())
    list1.sort()

    for i in range(n - 1):
        l = len(list1[i])
        if list1[i] == list1[i + 1][:l]:
            print("NO")
            break
    else:
        print("YES")

    
    
