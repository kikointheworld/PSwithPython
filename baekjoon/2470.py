'''
https://www.acmicpc.net/problem/2470
'''

import sys

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때
n = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
list1.sort()

if list1[0] > 0:
    print(list1[0], list1[1])
elif list1[-1] < 0:
    print(list1[-2], list1[-1])
else:
    i = 0
    j = -1
    mini = 1555555555

    ans1 = 0
    ans2 = 0
    while True:
        if i == n + j:
            break

        front = list1[i]
        end = list1[j]
        
        if mini > abs(front + end):
            mini = abs(front + end)
            ans1 = front
            ans2 = end
        
        if abs(front) >= abs(end):
            i += 1
        else:
            j -= 1
    
    print(ans1, ans2)
