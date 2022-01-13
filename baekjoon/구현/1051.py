'''
https://www.acmicpc.net/problem/1051
'''
import sys
# input = sys.stdin.readline

n, m = map(int, input().split())

nums = []

for _ in range(n):
    nums.append(input())

mini = min(n, m)

for i in range(mini - 1, 0, -1): # (i + 1) ** 2 만큼이 크기일 것이다. 
    for j in range(n):
        for k in range(m):
            tmp = nums[j][k]
            if j + i < n and k + i < m:
                if nums[j + i][k] == tmp and nums[j][k + i] == tmp and nums[j + i][k + i] == tmp:
                    print((i + 1) ** 2)
                    exit()

print(1)
