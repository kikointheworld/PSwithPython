'''
https://www.acmicpc.net/problem/2776
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    list1 = list(map(int, sys.stdin.readline().split()))
    list1.sort()
    m = int(sys.stdin.readline())
    list2 = list(map(int, sys.stdin.readline().split()))
    for i in range(m):
        start = 0
        end = n - 1

        target = list2[i]

        if target < list1[start] or target > list1[end]:
            print(0)
            continue

        while start <= end:
            mid = (start + end) // 2

            if list1[mid] == target:
                print(1)
                break
            elif list1[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if list1[mid] !=  target:
            print(0)
