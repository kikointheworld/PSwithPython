# 16:40

import sys
from collections import deque
from itertools import permutations

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1, 2, 2], [4, 5, 6], [7, 8, 9]]

if list1 == list2:
    print(0)
else:
    print(-1)
