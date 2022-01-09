'''
https://www.acmicpc.net/problem/1246
'''

n, m = map(int, input().split())
list1 = []
ans = 0
for _ in range(m):
  list1.append(int(input()))

list1.sort()
price = 0
for i in range(m):
  if (n >= (m - i)) and ((m - i) * list1[i] > ans) :
    ans = (m - i) * list1[i] 
    price = list1[i]

print(price, ans)
