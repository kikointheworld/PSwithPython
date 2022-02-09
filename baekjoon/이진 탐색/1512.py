'''
https://www.acmicpc.net/problem/2512
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
prices = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

prices.sort()

sum_of_prices = sum(prices)

# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정
if sum_of_prices <= m:
    print(prices[-1])
else: # 그 이외에 경우..
    ans = 0

    start = 0
    end = prices[-1]

    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for i in range(n):
            if mid > prices[i]:
                tmp += prices[i]
            else:
                tmp += mid
        
        if tmp > m:
            end = mid - 1
        else:
            start = mid + 1
            ans = mid if mid > ans else ans
            


    print(ans)

    
