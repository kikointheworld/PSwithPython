'''
https://www.acmicpc.net/problem/18870
'''
import sys

n = int(sys.stdin.readline())

list1 = list(map(int,sys.stdin.readline().split()))

t1 = set(list1)
list2 = list(t1)
list2.sort()

dic1 = {}

for i in range(0, len(list2)):
    dic1[list2[i]] =  i 

for i in range(n):
    print(dic1[list1[i]], end = " ")
