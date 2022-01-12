'''
https://www.acmicpc.net/problem/1292
'''

a, b = map(int, input().split())
ans = 0
count = 0 
for i in range(1, 99999):

    for j in range(i):
        count += 1
        if count >= a and count <= b:
            ans += i
        if count == b:
            break
    if count == b:
            break
print(ans)       


