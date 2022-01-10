'''
https://www.acmicpc.net/problem/20044
'''

n = int(input())

list1 = list(map(int, input().split()))

list1.sort()
ans = 10000001

for i in range(len(list1) // 2):
  if ans > list1[i] + list1[-i -1]:
    ans = list1[i] + list1[-i -1]
print(ans)
