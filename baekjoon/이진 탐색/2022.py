'''
https://www.acmicpc.net/problem/2022
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
import math
sys.setrecursionlimit(100000)

x, y, c = map(float,sys.stdin.readline().split())

start = 0
end = min(x, y)

def calculator(x, y, z, c):
    tmpb1 = math.sqrt((x ** 2) - (z ** 2) )
    tmpb2 = math.sqrt((y ** 2) - (z ** 2) )
    b = round((tmpb1 * tmpb2)/(tmpb1 + tmpb2), 4)
    if abs(c-b) <=0.0001:
        return 1
    elif c>b:
        return 0
    else:
        return -1




while start <= end:
    mid = (start + end )/2
    tmp = calculator(x, y, mid, c)
    
    
    if tmp == 1:
        print("%.03f"%mid)
        exit()
    elif tmp == -1:
        start = mid
    else:
        end = mid


