from inspect import stack
import sys
from collections import deque

# https://www.acmicpc.net/problem/10799

# input_data = sys.stdin.readline().rstrip()
# # rstrip()해야 이게 공백없이 출력됨.
# data = list(map(int, sys.stdin.readline().split()))

n = sys.stdin.readline().rstrip()
n = n.replace("()", ".")
inputList = deque(list(n))

stackList = deque([])

ans = 0

while(inputList):
    currentValue = inputList.popleft()
    if currentValue == "(":
        stackList.append("(")
        ans += 1
    elif currentValue == ")":
        stackList.pop()
    elif currentValue == ".":
        ans += len(stackList)


print(ans)
