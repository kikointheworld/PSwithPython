'''
https://www.acmicpc.net/problem/2331
'''
import sys
# input = sys.stdin.readline

a, p = map(int, input().split())

d = []
d.append(a)

# i = 0
while(True):
    # i += 1

    tmp = d[-1]
    val = 0

    while tmp:
        val += ((tmp % 10) ** p)
        tmp //= 10

    

    # tmp += int((d[-1] % 10)) ** p
    #tmp += int((d[-1] / 10) % 10 ) ** p
    #tmp += int((d[-1] / 100) % 10 ) ** p
    #tmp += int((d[-1] / 1000) % 10) ** p

    if val in d:
        print(d.index(val))
        break
    else:
        d.append(val)

        
