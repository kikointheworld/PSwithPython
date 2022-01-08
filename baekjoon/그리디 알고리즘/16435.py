'''
https://www.acmicpc.net/problem/16435
'''

n, l = map(int, input().split())

h = list(map(int, input().split()))

h.sort()

ans = l
for i in h:
    if ans >= i:
        ans += 1
print(ans)
        