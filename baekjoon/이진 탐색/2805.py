'''
https://www.acmicpc.net/problem/2805
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
sys.setrecursionlimit(100000)

n, m = map(int,sys.stdin.readline().split())

list1 = list(map(int, sys.stdin.readline().split()))


list1.sort()

start = 0
end = list1[-1]

ans = 0
while (start <= end):
    mid = (start + end) // 2
    
    tmp = 0

    for i in list1:
        if i - mid > 0:
            tmp += (i - mid)
        if tmp > m:
            break
        
    if tmp >= m:
        # ans = mid if mid > ans else ans
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)

