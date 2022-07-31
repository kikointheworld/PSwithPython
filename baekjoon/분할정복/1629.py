import sys

def dcPower(a, b, c):
    if b == 0: 
        return 1;
    if b == 1:
        return a % c
    
    if (b % 2 == 0):
        ret = dcPower(a, b / 2, c)
        return (ret * ret)  % c
    else:
        ret = dcPower(a, (b-1) / 2, c)
        return (ret * ret * a)  % c



a, b, c = map(int, sys.stdin.readline().split())

print(dcPower(a, b, c))
