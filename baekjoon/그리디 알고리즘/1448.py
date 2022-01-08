'''
https://www.acmicpc.net/problem/1448
'''
import sys
n = int(sys.stdin.readline().rstrip())
list1 = []
for i in range(n):
  list1.append(int(sys.stdin.readline().rstrip()))

list1.sort(reverse=True)

ans = -1

for i in range(n - 2):
  if list1[i] < list1[i + 1] + list1[i +2]:
    ans = list1[i] + list1[i + 1] + list1[i +2]
    break
print(ans)
