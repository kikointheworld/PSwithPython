from collections import deque

qs = [deque() for _ in range(4)]
for q in qs:
    for i in range(1, 5):
        q.append((i, i))
qs[0] = qs[0] + qs[1]
qs[1] = deque()

for q in qs:
    print(q)
