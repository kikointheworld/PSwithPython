import sys
from collections import deque

# https://www.acmicpc.net/problem/1935

# input_data = sys.stdin.readline().rstrip()
# # rstrip()해야 이게 공백없이 출력됨.
# data = list(map(int, sys.stdin.readline().split()))

n = int(sys.stdin.readline().rstrip())

strList = sys.stdin.readline().rstrip()

intList = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

stackList = deque([])

while(strList):
    current = strList[0]
    strList = strList[1:]

    if current == "+":
        a = stackList.pop()
        b = stackList.pop()
        stackList.append(a + b)

    elif current == "-":
        a = stackList.pop()
        b = stackList.pop()
        stackList.append(b - a)

    elif current == "*":
        a = stackList.pop()
        b = stackList.pop()
        stackList.append(a * b)

    elif current == "/":
        a = stackList.pop()
        b = stackList.pop()
        stackList.append(b / a)
    
    else:
        stackList.append(intList[ord(current) - 65])
    

print('%.2f'%stackList.pop())
