'''
https://www.acmicpc.net/problem/13706
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())


start = 1
end = n

while start <= end:
    mid = (start + end) // 2

    tmp = mid ** 2

    if tmp == n:
        print(mid)
        exit()
    elif tmp > n:
        end = mid - 1
    else:
        start = mid + 1
    
