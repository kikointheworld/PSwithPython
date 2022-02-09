'''
https://www.acmicpc.net/problem/2343
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
sys.setrecursionlimit(100000)

n, m = map(int,sys.stdin.readline().split())

list1 = list(map(int, sys.stdin.readline().split()))

start = max(list1)
end = start * n
# 블루레이 크기가 이상적인것, 그리고 ㅈㄴ큰것 사이에서하면.. 될듯?
ans = sys.maxsize
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    count = 0

    for i in range(n):
        if tmp + list1[i] > mid:
            tmp = 0
            count += 1
        tmp += list1[i]

    if tmp != 0:
        count += 1
    if count <= m:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
