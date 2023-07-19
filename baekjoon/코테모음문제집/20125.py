

n = int(input())
MAP = [input() for i in range(n)]


def in_map(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False


for i in range(1, n - 1):
    for j in range(1, n - 1):
        if MAP[i][j] == "*" and MAP[i-1][j] == "*" and MAP[i+1][j] == "*" and MAP[i][j-1] == "*" and MAP[i][j+1] == "*":
            print(i + 1, j + 1)

            # 왼쪽 팔
            tmp = 0
            for k in range(1, n):
                if in_map(i, j - k) and MAP[i][j - k] == "*":
                    tmp += 1
                else:
                    break
            print(tmp, end=' ')

            # 오른쪽 팔
            tmp = 0
            for k in range(1, n):
                if in_map(i, j + k) and MAP[i][j + k] == "*":
                    tmp += 1
                else:
                    break
            print(tmp, end=' ')

            # 허리
            tmp = 0
            for k in range(1, n):
                if in_map(i + k, j) and MAP[i + k][j] == "*":
                    tmp += 1
                else:
                    break
            print(tmp, end=' ')

            left_leg_y, left_leg_x = i + tmp + 1, j - 1
            right_leg_y, right_leg_x = i + tmp + 1, j + 1

            # print("left", left_leg_y, left_leg_x)
            # print("right", right_leg_y, right_leg_x)

            # 허리
            tmp = 1
            for k in range(1, n):
                if in_map(left_leg_y + k, left_leg_x) and MAP[left_leg_y + k][left_leg_x] == "*":
                    tmp += 1
                else:
                    break
            print(tmp, end=' ')

            # 허리
            tmp = 1
            for k in range(1, n):
                if in_map(right_leg_y + k, right_leg_x) and MAP[right_leg_y + k][right_leg_x] == "*":
                    tmp += 1
                else:
                    break
            print(tmp)

            break
