'''
https://www.acmicpc.net/problem/19941
'''

n, k = map(int, input().split())

s = input()

ans = 0

dp = [0]* n
dh = [0] * n

for i in range(n):
    if s[i] == 'P':
        dp[i] = 1
    elif s[i] == 'H':
        dh[i] = 1

for i in range(n):
    if dp[i] == 1:
        for j in range(-k, k + 1):
            if (i + j) >= 0 and (i + j) < n:
                if dh[i + j] == 1:
                    ans += 1
                    dh[i + j] = 0
                    break

print(ans)


    