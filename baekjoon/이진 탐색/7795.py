'''
https://www.acmicpc.net/problem/7795
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
from unicodedata import mirrored
sys.setrecursionlimit(100000)

t = int(sys.stdin.readline())


for _ in range(t):
    n, m = map(int,sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    B.sort()

    tmp = 0
    for i in range(n):
        target = A[i]

        start = 0
        end = m - 1
        answer = -1
        while start <= end:
            mid = (start + end) // 2
            if B[mid] < target:
                answer = mid
                start = mid + 1
            else:
                end = mid - 1
        answer+= 1
        # print(answer)
        tmp += answer
    print(tmp)
    
