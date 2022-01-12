'''
https://www.acmicpc.net/problem/11866
'''

n, k = map(int, input().split())

people = list(range(1, n + 1))

for i in range(n):
    for _ in range(k - 1):
        people.append(people.pop(0))
    
    if i == 0 and n == 1:
        print("<" + str(people.pop(0)), end =">")

    elif i == 0:
        print("<" + str(people.pop(0)) + ", ", end ="")
    elif i == n - 1:
        print(str(people.pop(0)) + ">", end ="")
    else:
        print(people.pop(0), end = ", ")
