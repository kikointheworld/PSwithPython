'''
https://www.acmicpc.net/problem/11051
이항정리 --> 파스칼의 삼각형으로 다이내믹 프로그래밍으로 해결
'''
import sys
n, k =  map(int,sys.stdin.readline().split())


d = []
for _ in range(n + 1):
    d.append([0] * (n + 1))

    
for i in range(n + 1):
    for j in range(n + 1):
        if i==j or j == 0:
            d[i][j] = 1
        else:
            d[i][j] = (d[i-1][j-1] + d[i-1][j]) % 10007



print(d[n][k])
