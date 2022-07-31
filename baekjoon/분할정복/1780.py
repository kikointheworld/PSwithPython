import sys

ans = [0, 0, 0]

def isMinusOne(x, y, len):
    for i in range(len):
        for j in range(len):
            if arr[x + i][y + j] != -1:
                return False
    return True


def isZero(x, y, len):
    for i in range(len):
        for j in range(len):
            if arr[x + i][y + j] != 0:
                return False
    return True

def isOne(x, y, len):
    for i in range(len):
        for j in range(len):
            if arr[x + i][y + j] != 1:
                return False
    return True




def func(x, y, len):
    if len == 1: # 크기가 1일떄 처리
        if arr[x][y] == 0:
            ans[0] += 1
            return
        elif arr[x][y] == 1:
            ans[1] += 1
            return
        else:
            ans[-1] += 1
            return

    if isZero(x, y, len):
        ans[0] += 1
        return
    if isOne(x, y, len):
        ans[1] += 1
        return
    if isMinusOne(x, y, len):
        ans[-1] += 1
        return
    
    len = len // 3
    
    func(x, y, len)
    func(x, y + len, len)
    func(x, y + len*2, len)
    
    func(x + len, y, len)
    func(x + len, y + len, len)
    func(x + len, y + len*2, len)

    func(x + len*2, y, len)
    func(x + len*2, y + len, len)
    func(x + len*2, y + len*2, len)


n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
func(0, 0, n)

print(ans[-1]) # -1
print(ans[0]) # 0 
print(ans[1]) # 1
