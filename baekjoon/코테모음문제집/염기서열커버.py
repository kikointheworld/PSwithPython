import sys


def input():
    return sys.stdin.readline().rstrip()


def checker(new, dna):
    tmp = ''
    flag = True
    for i in range(m):
        # . 이면 어떤게 와도 됨.
        if dna[i] == '.':
            # new 가 값 들어오면 값으로 바꾸고, .이면 그대로~
            tmp += new[i]
            continue
        # 기존에 특정값으로 정해짐.
        if new[i] == '.':
            tmp += dna[i]
            continue
        if new[i] == dna[i]:
            tmp += dna[i]
            continue

        # 단 둘다 다른 값이면 쉴드불가
        flag = False
        tmp = dna

    return tmp, flag


n, m = map(int, input().split())
dnas = [input() for _ in range(n)]
ans_list = [dnas[0]]
ans = 1
for i in range(n):
    new = dnas[i]

    for j in range(ans):
        dna = ans_list[j]
        ans_list[j], flag = checker(new, dna)

        if flag:
            break
    if flag:
        continue
    else:
        ans_list.append(new)
        ans += 1


print(ans)
