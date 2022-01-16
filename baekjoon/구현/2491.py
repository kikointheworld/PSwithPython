'''
https://www.acmicpc.net/problem/2491
'''
n = int(input())

list1 = list(map(int, input().split()))

ans = 1
increase = 1
decrease = 1

for i in range(1, n):
    if list1[i - 1] <= list1[i]:
        increase += 1
        ans = increase if ans < increase else ans
    else:
        increase = 1


for i in range(1, n):
    if list1[i - 1] >= list1[i]:
        decrease += 1
        ans = decrease if ans < decrease else ans
    else:
        decrease = 1
        
print(ans)
