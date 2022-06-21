import sys
input = sys.stdin.readline
'''
https://www.acmicpc.net/problem/11478
'''
#sys.setrecursionlimit(10000)

S = input().rstrip()
l = len(S)
ans_set = set([])
for i in range(l):
    for j in range(1, l + 1):
        if i + j > l :
            break
        ans_set.add(S[i:i+j])
# print(ans_set)
print(len(ans_set))
