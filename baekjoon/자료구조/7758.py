'''
https://www.acmicpc.net/problem/7758
'''
import sys

n = int(sys.stdin.readline())
people = {}
for _ in range(n):
  name, status = sys.stdin.readline().rstrip().split()

  if status == "enter":
    people[name] = 1
  else:
    if people[name]:
      del people[name]
    

for i in sorted(people, reverse=True):
  print(i)
