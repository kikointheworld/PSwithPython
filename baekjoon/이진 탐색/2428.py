'''
https://www.acmicpc.net/problem/2428
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

files = list(map(int, sys.stdin.readline().split()))

files.sort()

ans = 0

for i in range(n):
    target = (10/9) * files[i]

    start = 0
    end = n - 1 - i

    tmp = 0

    while (start <= end):
        mid = (start + end) //2

        if files[i + mid] <= target:
            start = mid + 1
            tmp = mid
        else:
            end = mid - 1
        
    ans += tmp
    # print(start, end)
print(ans)

