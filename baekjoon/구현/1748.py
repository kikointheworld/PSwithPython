'''
https://www.acmicpc.net/problem/1748
'''
import sys

tmp = sys.stdin.readline().rstrip()

n = int(tmp)

n_len = len(tmp)
ans = 0



for i in range(1, n_len + 1):
    if i == n_len:
        ans += (n - 10 ** (i - 1) + 1) * i
    else:
        ans += i * 9 * (10 ** (i - 1))

print(ans)

