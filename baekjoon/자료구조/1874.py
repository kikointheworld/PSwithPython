from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
stack = []
ans_num = []
origin_list = []
ans = []
cnt = 1
for i in range(n):
    now = int(input())
    origin_list.append(now)
    while (True and cnt <= n):
        if len(stack) != 0 and stack[-1] == now:
            stack.pop()
            ans.append('-')
            ans_num.append(now)
            break
        ans.append('+')
        stack.append(cnt)
        cnt += 1

while (stack):
    now = stack.pop()
    ans_num.append(now)
    ans.append('-')

if ans_num == origin_list:
    for i in ans:
        print(i)
else:
    print('NO')
