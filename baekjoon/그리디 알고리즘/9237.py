'''
https://www.acmicpc.net/problem/9237
'''

n = int(input())

list1 = list(map(int, input().split()))

list1.sort(reverse=True)

ans = 0

for i in range(n):
    if (i + 2) + list1[i] > ans :
        ans = (i + 2) + list1[i]
    
    


print(ans)