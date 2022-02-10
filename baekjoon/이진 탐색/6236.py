'''
https://www.acmicpc.net/problem/6236
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
from unicodedata import mirrored
sys.setrecursionlimit(100000)

n, m = map(int,sys.stdin.readline().split())

list1 = []

for _ in range(n):
    list1.append(int(sys.stdin.readline()))

ans = 0
end = sum(list1)
start = max(list1)

while start <= end:
    mid = (start + end) // 2

    count = 1
    tmp = mid

    for i in range(n):
        if tmp - list1[i] < 0:
            tmp = mid
            count += 1
        tmp -= list1[i]   
    
    if count > m:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1


print(ans)  
