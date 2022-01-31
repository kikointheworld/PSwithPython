'''
https://www.acmicpc.net/problem/1904

dp문제는 한개씩 돌려보고.. 규칙성을 파악하는게 중요한듯.
괜히 조합으로 풀려고 하다가 이중리스트 구현하느라 메모리 오버나고..
그냥 피보나치로 풀리는 문제였다
'''
import sys
n =  int(sys.stdin.readline())
d = [0] * 1000001

d[1] = 1
d[2] = 2
for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i  - 2]) % 15746
print(d[n])
