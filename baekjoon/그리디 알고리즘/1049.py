'''
https://www.acmicpc.net/problem/1049
'''

n, m = map(int, input().split())


price1 = 9999999999
price6 = 9999999999


for _ in range(m):
  a, b = map(int, input().split())
  if price1 > b:
    price1 = b
  if price6 > a:
    price6 = a
  if price6 > 6*b:
    price6 = 6*b



print(   min(price6*(n // 6) + price6, price6*(n // 6) + price1 * (n % 6)))
