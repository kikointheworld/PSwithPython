s = input()

ans = 0

tmp = s[0]

q = s[0]

for i in range(len(s)):
    if s[i] != tmp:
        tmp = s[i]
        q += s[i]
        ans += 1
print(len(q) // 2)