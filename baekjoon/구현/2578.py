'''
https://www.acmicpc.net/problem/2578
'''
import sys
# input = sys.stdin.readline

bingo = []

for _ in range(5):
    bingo.append(list(map(int, input().split())))

ans = 0

numbers = []

for _ in range(5):
    numbers.append(list(map(int, input().split())))
    

for j in range(5):
    for m in range(5):
        tmp = numbers[j][m]

        for q in range(5):
            for p in range(5):
                if bingo[q][p] == tmp:
                    bingo[q][p] = 0
                    ans += 1

        # check bingos
        lines = 0
        # 대각선 체크
        if bingo[2][2] == 0:
            if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[3][3] == 0 and bingo[4][4] == 0:
                lines += 1
            if bingo[0][4] == 0 and bingo[1][3] == 0 and bingo[3][1] == 0 and bingo[4][0] == 0:
                lines += 1


        for k in range(5):
            # 가로선 체크
            if bingo[k][0] == 0 and bingo[k][1] == 0 and bingo[k][2] == 0 and bingo[k][3] == 0 and bingo[k][4] == 0 :
                lines += 1
            
            # 세로선 체크
            if bingo[0][k] == 0 and bingo[1][k] == 0 and bingo[2][k] == 0 and bingo[3][k] == 0 and bingo[4][k] == 0 :
                lines += 1
        
        if lines >= 3:
            print(ans)
            exit()
