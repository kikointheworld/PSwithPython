'''
https://www.acmicpc.net/problem/1758
'''

import sys
n = int(sys.stdin.readline())

list1 = []

for i in range(n):
    list1.append(int(sys.stdin.readline()))

list1.sort(reverse=True)

ans = sum(list1)

for i in range(2, n, 3):
    ans -= list1[i]

print(ans)
