'''
https://www.acmicpc.net/problem/16401
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
sys.setrecursionlimit(100000)
m, n = map(int,sys.stdin.readline().split())

cookies = list(map(int, sys.stdin.readline().split()))

cookies.sort()

start = 1
end = cookies[-1]

while start <= end:
    mid = (start + end) // 2
    count = 0

    for cookie in cookies:
        tmp = 0
        i = cookie
        if i < mid:
            continue
        while True:
            tmp += mid
            i -= mid
            count += 1

            if i - mid < 0:
                break
        
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(start - 1)

