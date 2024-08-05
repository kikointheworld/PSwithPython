from itertools import permutations

def solution(numbers):
    INF = 10000000
    answer = 0
    dp = [1] * INF
    dp[0], dp[1] = 0, 0
    visited = [0] * INF
    for i in range(2, int( INF ** 0.5) + 1):
        for j in range(i * 2, INF, i):
            dp[j] = 0

                
    list1 = []
    for i in numbers:
        list1.append(i)
        
    for i in range(1, len(numbers) + 1):
        for j in permutations(list1, i):
            tmp = j[0]
            for k in range(1, len(j)):
                tmp += j[k]
            int_tmp = int(tmp)
            if dp[int_tmp]:
                if not visited[int_tmp]:
                    visited[int_tmp] = 1
                    answer += 1
                    
    return answer
