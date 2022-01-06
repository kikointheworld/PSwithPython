'''
https://www.acmicpc.net/problem/1449
'''

n, l = map(int, input().split())

list1 = list(map(int, input().split()))

list1.sort()

ans = 0

flag = 0

target = 0

for i in range(n):
    if i == 0:
        target = list1[i] + l - 1
        ans += 1
    
    else:
        if list1[i] <= target:
            continue
        else:
            ans += 1
            target = list1[i] + l - 1


print(ans)