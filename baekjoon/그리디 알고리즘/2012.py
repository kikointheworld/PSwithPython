'''
https://www.acmicpc.net/problem/2012
'''

import sys
n = int(sys.stdin.readline())

score = []

for i in range(n):
    score.append(int(sys.stdin.readline()))

score.sort()

ans = 0

for i in range(n):
    ans += abs(i + 1 - score[i])

print(ans)
