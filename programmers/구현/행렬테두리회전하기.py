# 20:12 20:24
def rotate(MAP, y1, x1, y2, x2):
    tmp = MAP[y1][x1]
    ans = tmp
    for i in range(x1 + 1, x2 + 1):
        MAP[y1][i], tmp = tmp, MAP[y1][i]
        ans = min(ans, tmp)
    for i in range(y1 + 1, y2 + 1):
        MAP[i][x2], tmp = tmp, MAP[i][x2]
        ans = min(ans, tmp)
    for i in range(x2-1, x1-1, -1):
        MAP[y2][i], tmp = tmp, MAP[y2][i]
        ans = min(ans, tmp)
    for i in range(y2-1, y1-1, -1):
        MAP[i][x1], tmp = tmp, MAP[i][x1]
        ans = min(ans, tmp)
    return ans


def solution(rows, columns, queries):
    n, m = rows, columns
    MAP = [[i + j * m for i in range(1, m + 1)] for j in range(n)]
    # originalMap = copy.deepcopy(MAP)
    ans = []
    for x1, y1, x2, y2 in queries:
        ans.append(rotate(MAP, x1 - 1, y1 - 1, x2 - 1, y2 - 1))

    return ans
