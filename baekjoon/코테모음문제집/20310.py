words = input()
list1 = [0, 0]

for i in words:
    list1[int(i)] += 1

list1[0] //= 2
list1[1] //= 2

ans = ""

# 0은 가급적 빨리, 1은 최대한 뒤로.
for i in words:
    if i == '0' and list1[0]:
        ans += '0'
        list1[0] -= 1
    elif i == "1":
        if list1[1] > 0:
            list1[1] -= 1
        else:
            ans += '1'


print(ans)

