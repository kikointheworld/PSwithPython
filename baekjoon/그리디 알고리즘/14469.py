'''
https://www.acmicpc.net/problem/14469
'''
n = int(input())
list1 = []
for i in range(n):
  list1.append(list(map(int, input().split())))
  list1.sort(key=lambda x : [x[0], x[1]])

ans = list1[0][0] + list1[0][1]

for j in range(1, n):
  if ans < list1[j][0]:
    ans = list1[j][0] + list1[j][1]
  else:
    ans += list1[j][1]
print(ans)
