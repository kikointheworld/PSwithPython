INF = 10 ** 9

def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = 0, 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    cop = min(cop, max_cop)
    alp = min(alp, max_alp)
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i < max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= i and cop_req <= j:
                    new_alp = min(max_alp, i + alp_rwd)
                    new_cop = min(max_cop, j + cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost) 

    return dp[max_alp][max_cop]
