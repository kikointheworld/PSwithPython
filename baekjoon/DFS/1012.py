'''
https://www.acmicpc.net/problem/1012
'''
import sys
sys.setrecursionlimit(100000)
def dfs(a, b):

    # 상
    if a <= -1 or a >= n or b <= -1 or b >= m:
        return
    if ground[a][b] == 1:
        ground[a][b] = 0
        if a - 1 >= 0:
            dfs(a - 1, b)
        if a + 1 <= n - 1:
            dfs(a + 1, b)
        if b - 1 >= 0:
            dfs(a, b - 1)
        if b + 1 <= m - 1:    
            dfs(a, b + 1)

    return


t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    
    ground = [[0] * m for _ in range(n)]
    
    for j in range(k):
        x, y = map(int, input().split())
        ground[y][x] = 1
    
    ans = 0

    for c in range(n):
        for v in range(m):
            if ground[c][v] == 1:
                dfs(c, v)
                ans += 1
    print(ans)
