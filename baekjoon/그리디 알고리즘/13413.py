'''
https://www.acmicpc.net/problem/13413
'''
n = int(input())
for i in range(n):
  l = int(input())
  a = input()
  b = input()
  ans = 0
  WtoB = 0
  BtoW = 0

  for j in range(l):
    if a[j] == 'W' and b[j] == 'B':
      WtoB += 1
    elif a[j] == 'B' and b[j] == 'W':
      BtoW += 1
  print(max(WtoB, BtoW))
    

