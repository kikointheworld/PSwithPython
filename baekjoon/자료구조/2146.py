import sys
from collections import deque

# https://www.acmicpc.net/problem/2164

# input_data = sys.stdin.readline().rstrip()
# # rstrip()해야 이게 공백없이 출력됨.
# data = list(map(int, sys.stdin.readline().split()))

n = int(sys.stdin.readline().rstrip())

list1 = deque([i for i in range(1, n + 1)])
tmp = list1.popleft()

while(list1):
    list1.append(list1.popleft())
    tmp = list1.popleft()
print(tmp)



