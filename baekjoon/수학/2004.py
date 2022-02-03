'''
https://www.acmicpc.net/problem/2004
'''

import sys

n, m = map(int,sys.stdin.readline().split())

def function1 (n, k):
    ans = 0
    while n:
        n //= k 
        ans += n
    return ans

five = function1(n, 5) - function1(m, 5) - function1(n-m, 5)
two = function1(n, 2) - function1(m, 2) - function1(n-m, 2)

print(min(five, two))
