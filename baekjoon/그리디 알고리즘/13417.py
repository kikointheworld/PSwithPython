'''
https://www.acmicpc.net/problem/13417
'''

n = int(input())
for _ in range(n):
  tmp = int(input())
  tmp_list = list(map(str, input().split()))
  ans = tmp_list[0]
  
  for i in range(1, tmp):
    if ord(ans[0]) < ord(tmp_list[i]):
      ans = ans + tmp_list[i]
    else:
      ans = tmp_list[i] + ans

  
  print(ans)
