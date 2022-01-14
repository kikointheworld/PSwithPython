'''
https://www.acmicpc.net/problem/1244
'''
import sys
# input = sys.stdin.readline

n = int(input())

s = list(map(int, input().split()))

students_num = int(input())

for j in range(students_num):
    sex, number = map(int, input().split())
    if sex == 1:
        for i in range(n):
            if (i + 1) % number == 0:
                if s[i] == 0:
                    s[i] = 1
                else:
                    s[i] = 0
    
    elif sex == 2:
        for k in range(n):
            if (number - 1) - k >= 0 and (number - 1) + k < n:
                if k == 0:
                    if s[number - 1] == 0:
                        s[number - 1] = 1
                    else:
                        s[number - 1] = 0
                else:
                    if s[number -1 - k] == s[number - 1 + k]:
                        if s[number -1 - k] == 1:
                            s[number -1 - k] = 0
                        else:
                            s[number -1 - k] = 1
                        
                        if s[number -1 + k] == 1:
                            s[number -1 + k] = 0
                        else:
                            s[number -1 + k] = 1
                    else:
                        break
            else:
                break

count = 0
for i in range(len(s)):
    count += 1
    if count % 20 == 0:
        print(s[i])
    else:
        print(s[i], end = " ")
