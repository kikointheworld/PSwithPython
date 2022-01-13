'''
https://www.acmicpc.net/problem/8979
'''
import sys
# input = sys.stdin.readline

n, k = map(int, input().split())

medal = []

score = [0] * n

for _ in range(n):
    tmp = list(map(int, input().split()))
    score[tmp[0] - 1] = tmp[1] * 1000000 + tmp[2] * 1 + tmp[3] * 0.000000001

rank = 1
for i in range(n):
    if score[k - 1] < score[i]:
        rank += 1

print(rank)

    
