from collections import deque

p = int(input())

for tc in range(p):
    data = list(map(int, input().split()))
    tc_num = data[0]
    ans = 0

    in_line = deque([data[1]])
    out_line = deque()  # stack
    wait_line = deque(data[2:])

    while (wait_line):
        now_student = wait_line.popleft()

        while (in_line and in_line[-1] > now_student):
            out_line.append(in_line.pop())

        in_line.append(now_student)

        while (out_line):
            in_line.append(out_line.pop())
            ans += 1

    print(tc_num, ans)
