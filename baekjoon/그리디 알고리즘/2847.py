'''
https://www.acmicpc.net/problem/2847
'''

n = int(input())

score = []

for i in range(n):
    score.append(int(input()))

max_score = score[-1]


ans = 0


for i in range(1, n):
    if score[n - 1 - i] >= score[n - i]:
        ans += (score[n - 1 - i] - score[n - i] + 1)
        score[n - 1 - i] = score[n - i] - 1

print(ans)