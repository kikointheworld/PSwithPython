'''
https://www.acmicpc.net/problem/1475
'''

s = input()

set_list = [0] * 10 # 0 to 9

for i in range(len(s)):
    set_list[int(s[i])] += 1


set_list[6] += set_list[9]
set_list[9] = 0

if set_list[6] % 2 == 0:
    set_list[6] = set_list[6] // 2
else:
    set_list[6] = 1 + (set_list[6] // 2)

print(max(set_list))
