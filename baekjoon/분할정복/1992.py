import sys
# sys.setrecursionlimit(10**7)

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
    if isZero(x, y, len):
        print("0", end = "")
        return
    if isOne(x, y, len):
        print("1", end = "")
        return

    print("(", end = "")
    len = len // 2
    func(x, y, len)
    func(x, y + len, len)
    func(x  + len, y, len)
    func(x + len, y + len, len)
    print(")", end = "")
    

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    arr.append(list(map(int, tmp)))

# print(arr)
func(0, 0, n)
