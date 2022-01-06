'''
https://www.acmicpc.net/problem/15904

문제 해결 아이디어:
맨앞 U, 그리고 띄어쓰기와 C-P-C가 순서대로 나오는지만 확인
'''

flag = 0

s = input()

for i in range(len(s)):
    if flag == 0 and (s[i] ) == "U":
        flag = 1
        continue
    if flag == 1 and (s[i] ) == "C":
        flag = 2
        continue
    if flag == 2 and (s[i] ) == "P":
        flag = 3
        continue
    if flag == 3 and (s[i] ) == "C":
        flag = 4
        break
    


if flag == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")