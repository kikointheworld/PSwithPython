'''
https://www.acmicpc.net/problem/1343

문제 해결 아이디어:
.이 있으면 . 은 그대로
XXXX가 되면.. AAAA, 
그 이후에 XX 가 되면.. BB
'''


s = input()

l = len(s)
i = 0
ans = ""
while(i < l):
    if s[i] == ".":
        ans += "."
    elif s[i:i+4] =="XXXX":
        ans += "AAAA"
        i += 3
    elif s[i:i+2] == "XX":
        ans += "BB"
        i += 1
    i += 1

if len(ans) != l:
    print(-1)
else:
    print(ans)