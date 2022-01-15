'''
https://www.acmicpc.net/problem/11576
'''
import sys
# input = sys.stdin.readline

a, b = map(int, input().split())

m = int(input()) # 숫자의 자리수

a_list = list(map(int,input().split()))


ans = 0
square_num = 1
for i in range(m - 1, -1, -1):
    ans += a_list[i] * square_num
    square_num *= a

b_list = []

square_num = 0
while(True):
    if b ** square_num > ans :
        break
    square_num += 1


for i in range(square_num - 1, -1, -1):
    tmp = ans // (b ** i)
    b_list.append(tmp)
    ans -= tmp * (b ** i)

for j in b_list:
    print(j, end= " ")


