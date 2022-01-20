'''
https://www.acmicpc.net/problem/1764
'''

n, m = map(int, input().split())

a = []
b = []
for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())

set1 = set(a)
set2 = set(b)

ans = list(set1 & set2)
ans.sort()
print(len(ans))
for i in ans:
    print(i)
