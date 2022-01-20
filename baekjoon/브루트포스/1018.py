'''
https://www.acmicpc.net/problem/1018
'''
import sys

n, m = map(int, input().split())

chess = []
check1 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW"]
check2 = [ "BWBWBWBW", "WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB"]

for _ in range(n):
    chess.append(input())

ans = []

for i in range(0, n - 7):
    for j in range(0, m - 7): # 모든 정사각형 하니씩 확인
        ans_value1 = 0 
        ans_value2 = 0 
        for a in range(0, 8):
            for b in range(0, 8):
                # check1
                if chess[i + a][j + b] != check1[a][b]:
                    ans_value1 += 1 
                if chess[i + a][j + b] != check2[a][b]:
                    ans_value2 += 1 

        ans.append(ans_value1)
        ans.append(ans_value2)

print(min(ans))
        
