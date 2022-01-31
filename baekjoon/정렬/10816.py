'''
https://www.acmicpc.net/problem/10816
'''
import sys
n = int(sys.stdin.readline())

tmp = list(map(int, sys.stdin.readline().rstrip().split()))

list1 = [0] * (20000001) # -10000000 -> 0, 0->10000000, 10000000 -> 20000000

for i in tmp:
    list1[i + 10000000] += 1

m = int(sys.stdin.readline())

tmp2 = list(map(int, sys.stdin.readline().rstrip().split()))

for j in tmp2:
    print(list1[j + 10000000], end =" ")

