'''
https://www.acmicpc.net/problem/5800
'''
import sys

n = int(sys.stdin.readline())

for i in range(1, n + 1):
  tmp_list = list(map(int,sys.stdin.readline().split()))
  tmp_n = tmp_list.pop(0)
  print("Class", i)
  print("Max", max(tmp_list), end = ", ")
  print("Min", min(tmp_list), end = ", ")

  tmp_list.sort()
  gap = 0

  for j in range(1, tmp_n):
    gap =  tmp_list[j] - tmp_list[j - 1] if gap < tmp_list[j] - tmp_list[j - 1] else gap

  print("Largest gap", gap)


