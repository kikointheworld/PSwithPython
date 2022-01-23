'''
https://www.acmicpc.net/problem/9461
'''
import sys
n = int(sys.stdin.readline().rstrip())

wave = [0] * 101
wave[1] = 1
wave[2] = 1
wave[3] = 1
wave[4] = 2
wave[5] = 2
wave[6] = 3
wave[7] = 4
wave[8] = 5
wave[9] = 7
wave[10] = 9


for i in range(11, 101):
  wave[i] = wave[i - 1] + wave[i - 5]


for _ in range(n):
  tmp = int(sys.stdin.readline().rstrip())

  print(wave[tmp])
