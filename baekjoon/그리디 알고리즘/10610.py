'''
https://www.acmicpc.net/problem/10610

문제 해결 아이디어 :
30으로 나누어 떨어진 다는 것은 10과 3으로 모두 나누어 떨어져야 한다.

1. 10으로 나누어 떨어진다. >> 맨 뒷 자리가 10이 있어야함.
2. 3으로 나누어 떨어진다. >> 모든 숫자의 합이 3으로 나누어 떨어진다.

이 2가지를 이용..
'''

n = str(input())

list1 = list(n)

ans = -1

list1.sort(reverse=True)

if list1[-1] == '0':
    tmp_sum = 0
    for i in list1[:-1]:
        tmp_sum += int(i)


    if tmp_sum % 3 == 0:
        ans = int(''.join(list1))

print(ans)