'''
https://www.acmicpc.net/problem/1213
'''
s = input()

items = [0] * 26

for i in range(len(s)):
    items[ord(s[i]) - 65] += 1

odd_num = 0
odd_value = 0
for i in range(26):
    if items[i] % 2 == 1:
        odd_num += 1
        odd_value = i

if odd_num > 1:
    print("I'm Sorry Hansoo")
elif odd_num == 0:
    ans = ""

    for i in range(26):
        if items[25 - i] != 0:
            ans = chr(90 - i) * (items[25 - i] // 2) +ans  + chr(90 - i) * (items[25 - i] // 2)
    print(ans)
else:
    ans = chr(65 + odd_value)
    items[odd_value] -= 1

    for i in range(26):
        if items[25 - i] != 0:

            ans = chr(90 - i) * (items[25 - i] // 2) + ans + chr(90 - i) * (items[25 - i] // 2)
    print(ans)