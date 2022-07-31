import sys
from collections import deque

list1 = []
list2 = []

n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    list1.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())

for i in range(m):
    list2.append(list(map(int, sys.stdin.readline().split())))

arr = []

for i in range(n):
    tmplist = []
    for h in range(k):
        tmp = 0
        for j in range(m):
            tmp += list1[i][j] * list2[j][h]
        tmplist.append(tmp)
    arr.append(tmplist)

for i in range(n):
    for j in range(k):
        print(arr[i][j], end = " ")
    print()
