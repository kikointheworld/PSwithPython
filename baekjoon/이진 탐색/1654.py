'''
https://www.acmicpc.net/problem/1654
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
sys.setrecursionlimit(100000)

n, k = map(int,sys.stdin.readline().split())

list1 = []

for _ in range(n):
    list1.append(int(sys.stdin.readline()))

list1.sort()

ans = 1

def num_count(value, k):
    ans = 0
    for i in range(n):
        ans += (list1[i] // value)
    if ans < k:
        return 0
    else:
        return 1 # 나눠진 갯수가 적을때 
    

def main_function(start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    tmp = num_count(mid, k)

    if tmp == 0:
        main_function(start, mid - 1)
    else:
        global ans
        if ans < mid:
            ans = mid
            main_function(mid + 1, end)
        else:
            main_function(mid + 1, end)
            main_function(start, mid - 1)
            

main_function(1, list1[-1])

print(ans)

