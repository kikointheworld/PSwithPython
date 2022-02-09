'''
https://www.acmicpc.net/problem/1072
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
import math
sys.setrecursionlimit(100000)
x, y = map(int,sys.stdin.readline().split())

def floor(z, x):
    return (z  * 100)// x

original_z = floor(y, x)

start = 1
end = x
ans = 10000000011

if original_z >= 99:
    print(-1)
    exit()

while start <= end:
    mid = (start + end) // 2

    if floor(mid + y, x + mid) > original_z:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1


print(ans)


    
