'''
https://www.acmicpc.net/problem/1476
'''

e, s, m = map(int, input().split())
a, b, c = 1, 1, 1

i = 1
while(True):
    if e==a and s ==b and m ==c:
        print(i)
        break

    a += 1
    b += 1
    c += 1

    if a >= 16:
        a -= 15
    if b >= 29:
        b -= 28
    if c >= 20:
        c -= 19

    i += 1
