import sys

input = sys.stdin.readline

n, m = map(int, sys.stdin.readline().split())
sets = set([input().rstrip() for _ in range(n)])

for i in range(m):
    set2 = set(map(str, input().rstrip().split(",")))
    sets -= set2
    print(len(sets))