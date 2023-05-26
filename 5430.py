from collections import deque
import sys
input = sys.stdin.readline


t = int(input())

for i in range(t):
    err = 0
    flag = 0

    p = list(str(input()).rstrip())
    n = int(input())
    lst = deque(input().strip()[1:-1].split(","))
    queue = deque(lst)

    if n == 0:
        queue = []

    # r_deq = deque()
    for i in range(len(p)):
        if p[i] == 'R':
            # lst.reverse()
            flag += 1
        elif p[i] == 'D':
            # print("here", len(lst), lst)
            if len(queue) == 0:
                err = 1
                break
            else:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if err == 1:
        print('error')
    elif flag % 2 == 0:
        print("[" + ",".join(queue) + "]")
    else:
        queue.reverse()
        print("[" + ",".join(queue) + "]")
