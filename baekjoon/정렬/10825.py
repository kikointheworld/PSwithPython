'''
https://www.acmicpc.net/problem/10825
'''

import sys

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때

n = int(sys.stdin.readline())

student = []

for _ in range(n):
    name, korean, english, math = map(str, sys.stdin.readline().split())
    korean, english, math = int(korean), int(english), int(math)
    student.append([korean, english, math, name])

student.sort(reverse = True)
a = sorted(student, key = lambda x : (-x[0], x[1], -x[2], x[3]))

for i in range(n):
    print(a[i][3])


