'''
https://www.acmicpc.net/problem/4796

문제 해결 아이디어 : 
전형적인 그리디 알고리즘
'''

list_l = []
list_p = []
list_v = []

while(True):
    a, b, c = map(int, input().split())
    if a == 0:
        break
    list_l.append(a)
    list_p.append(b)
    list_v.append(c)

for i in range(len(list_l)):
    l = list_l[i]
    p = list_p[i]
    v = list_v[i]

    ans = 0 

    ans += (l * (v // p))

    if l < (v % p):
        ans += l
    else:
        ans += (v % p)

    print("Case " + str(i + 1) + ":", ans)



