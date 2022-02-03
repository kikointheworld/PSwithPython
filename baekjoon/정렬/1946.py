'''
https://www.acmicpc.net/problem/1946
'''

import sys

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    score = []
    ans = 0
    for _ in range(n):
        s1, s2 = map(int,sys.stdin.readline().split())
        score.append([s1, s2])
    score.sort()
    target = score[0][1]
    for i in score:
        if score[0] == i:
            ans += 1
        elif target > i[1]:
            ans += 1
            target = i[1]
    print(ans)
