import sys
input = sys.stdin.readline
'''
https://www.acmicpc.net/problem/1269
'''
#sys.setrecursionlimit(10000)


n, m = map(int, input().strip().split())

A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

print(len(A - B) + len(B - A))
