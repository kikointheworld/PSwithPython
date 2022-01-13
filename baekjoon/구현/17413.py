'''
https://www.acmicpc.net/problem/17413
'''
import sys
# input = sys.stdin.readline

s = input()

start = -1
flag = 1

ans = ""
tmp = ""
for i in range(len(s)):
    if start < 0  and s[i] == "<" :
        start = i;
        ans += tmp
        flag = 0
        tmp = ""
        continue

    if start >= 0 and s[i] == ">":
        ans += s[start:i + 1]
        start = -1
        flag = 1
        tmp = ""
        continue
    if flag == 1:
        if s[i] == " ":
            ans += tmp + " "
            tmp = ""
        else:
            tmp = s[i] + tmp
    
    if i == len(s) - 1:
        ans = ans + tmp

print(ans)
