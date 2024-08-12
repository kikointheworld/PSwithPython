class Solution(object):
    def maximalRectangle(self, matrix):
        ans = 0
        n, m = len(matrix), len(matrix[0])
        heights = [[0] * m for _ in range(n)]
        widths = [[0] * m for _ in range(n)]
        if matrix[0][0] == "1":
            heights[0][0], widths[0][0] = 1, 1
            ans = 1
        for i in range(1, n):
            if matrix[i][0] == '1':
                heights[i][0] = heights[i-1][0] + 1
                ans = max(ans, heights[i][0])
                widths[i][0] = 1

        for i in range(1, m):
            if matrix[0][i] == '1':
                widths[0][i] = widths[0][i - 1] + 1
                ans = max(ans, widths[0][i])
                heights[0][i] = 1
        

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "1":
                    heights[i][j] = heights[i-1][j] + 1
                    widths[i][j] = widths[i][j-1] + 1

                    cnt = widths[i][j]
                    height = heights[i][j]

                    for k in range(cnt):
                        height = min(height, heights[i][j - k])
                        ans = max(ans, height * (1 + k))



        return ans
