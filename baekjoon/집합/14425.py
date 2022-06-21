import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10000)


n, m = map(int, input().strip().split())

S = {input().strip() for i in range(n)}
ans = 0

for i in range(m):
    if input().strip() in S:
        ans += 1

print(ans)
