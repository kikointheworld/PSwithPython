'''
https://www.acmicpc.net/problem/1543
'''

s = input()
target = input()


l = len(target)


ans = 0

start_word = target[0]


i = 0

while(i < len(s)):
    if target == s[i:i + l]:
        i += (l - 1)
        ans += 1

    i += 1        



print(ans)
