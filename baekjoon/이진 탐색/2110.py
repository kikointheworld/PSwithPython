'''
https://www.acmicpc.net/problem/2110
'''

# n, m = map(int,sys.stdin.readline().split())
# n = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split())) 띄어쓰기로 리스트 나와있을 때


import sys
sys.setrecursionlimit(100000)

n, c = map(int,sys.stdin.readline().split())

list1 = []

for _ in range(n):
    tmp = int(sys.stdin.readline())
    list1.append(tmp)

list1.sort()


start = 1
end = list1[-1] - list1[0]


# 해당 거리를 유지하면... 몇개 설치 가능?
def func(d):
    count = 1
    current_point = list1[0]

    for i in range(n):
        if current_point + d <= list1[i]:
            count += 1
            current_point = list1[i]
    return count
    

while start <= end:
    mid = (start + end) // 2

    if func(mid) >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
