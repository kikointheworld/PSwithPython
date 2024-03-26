from collections import deque


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def solution(n, k):
    ans = []
    q = deque([i for i in range(1, n + 1)])

    while (n > 1):
        fac = factorial(n - 1)
        num = q[(k - 1) // fac]
        ans.append(num)
        q.remove(num)
        n -= 1
        k %= fac

    ans.append(q[-1])
    return ans
