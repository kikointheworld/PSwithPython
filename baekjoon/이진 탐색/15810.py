'''
https://www.acmicpc.net/problem/15810
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
sys.setrecursionlimit(100000)
n, m = map(int,sys.stdin.readline().split())

balloons = list(map(int, sys.stdin.readline().split()))
balloons.sort()

start = 1
end = balloons[-1] * m

while start <= end:
    mid = (start + end) // 2

    tmp = 0

    for balloon in balloons:
        tmp += (mid // balloon)
    
    if tmp >= m:
        end = mid - 1
    else:
        start = mid + 1


print(start)
