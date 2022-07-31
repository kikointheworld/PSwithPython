# 분할 정복법 이용, 계속 반으로 쪼개면서..!
import sys

def func(arr, b, n):
    if b == 1:
        return arr
    
    if (b % 2 == 0):
        ret = func(arr, b / 2, n)
        return matrixMultiply(ret, ret, n)
    
    else:
        ret = func(arr, (b - 1)/2, n)
        return matrixMultiply(matrixMultiply(ret, ret, n), arr, n)


def matrixMultiply(arr1, arr2, n):
    ret = []
    for i in range(n):
        tmplist  = []
        for h in range(n):
            tmp = 0
            for j in range(n):
                tmp += arr1[i][j] * arr2[j][h]
                tmp = tmp % 1000 
            tmplist.append(tmp)
        ret.append(tmplist)
    return ret

n, b = map(int, sys.stdin.readline().split())

arr = []

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)

ans = func(arr, b, n)


# 정답 출력
for i in range(n):
    for j in range(n):
        print(ans[i][j] % 1000, end =" ")
    print()
