'''
https://www.acmicpc.net/problem/4949
'''
import sys
while(True):
  s = sys.stdin.readline().rstrip()
  if s == ".":
    break
  stack = []
  ans = "yes"
  for i in s:
    if i == "(":
      stack.append(1)
    elif i == "[":
      stack.append(2)
    elif i == ")":
      if len(stack) == 0:
        ans = "no"
        break
      tmp = stack.pop()
      if tmp == 1:
        continue
      else:
        ans = "no"
        break
    elif i == "]":
      if len(stack) == 0:
        ans = "no"
        break
      tmp = stack.pop()
      if tmp == 2:
        continue
      else:
        ans = "no"
        break
    else:
      continue

  if len(stack) != 0:
    ans = "no"
  print(ans)
