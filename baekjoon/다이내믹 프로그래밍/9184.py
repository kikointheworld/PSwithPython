'''
https://www.acmicpc.net/problem/9184
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
import math
sys.setrecursionlimit(100000)

d = []

for _ in range(21):
    dr = []
    for _ in range(21):
        dr.append([0] * 21)
    d.append(dr)

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        d[0][0][0] = 1
        return d[0][0][0]
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if d[a][b][c] != 0:
        return d[a][b][c]

    if a < b and b < c:
        d[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return d[a][b][c]

    else:
        d[a][b][c] = w(a-1, b, c) + w(a-1, b -1,c) + w(a-1, b, c - 1) - w(a-1, b-1, c-1)
        return d[a][b][c]
        

while True:
    a, b, c = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break

    print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(w(a, b, c)))
