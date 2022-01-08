'''
https://www.acmicpc.net/problem/19939
'''

n, k = map(int, input().split())

n -= (k * (k + 1)) // 2

if n < 0:
    print(-1)
else:
    if n % k == 0:
        print(k - 1)
    else:
        print(k)