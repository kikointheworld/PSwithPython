def solution(triangle):
    
    l = len(triangle)
    
    for i in range(1, l):
        # 0일때
        triangle[i][0] += triangle[i - 1][0]
        # 나머지일때
        for j in range(1, i ):
            triangle[i][j] += max(triangle[i-1][j - 1], triangle[i-1][j])
        # i일 때  
        triangle[i][-1] += triangle[i - 1][-1]
    
    
    return max(triangle[-1])

# def solution(triangle):
#     ans = 1
    
#     n = len(triangle)
#     dp = []
#     for i in range(n):
#         dp.append([0] * (i + 1))
#     dp[0][0] = triangle[0][0]
#     if n == 1:
#         return dp[0][0]
    
#     for i in range(1, n):
#         dp[i][0], dp[i][i] = triangle[i][0] + dp[i - 1][0],triangle[i][i] + dp[i - 1][-1]
#         for j in range(1, i):
#             dp[i][j] = triangle[i][j] + max(dp[i-1][j - 1], dp[i-1][j])
            
#     # print(dp)
    
#     return max(dp[n - 1])
