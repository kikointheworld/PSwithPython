'''
https://www.acmicpc.net/problem/1439

문제 해결 아이디어 :
연속된 0과 1 중복되는 것을 중복 안되게끔 만들어주고, 
2의 몫을 구했다.
'''

s = input()

tmp = s[0]

q = s[0]

for i in range(len(s)):
    if s[i] != tmp:
        tmp = s[i]
        q += s[i]
        
print(len(q) // 2)