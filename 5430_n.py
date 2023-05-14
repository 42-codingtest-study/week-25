import sys
input = sys.stdin.readline
from collections import deque
import time
start_time = time.time()

t = int(input())

for _ in range (t):
    func = input().rstrip()
    l = int(input().rstrip())
    arr = list(map(int, input().rstrip()[1:-1].replace(',','')))
    
    cnt = 0
    for i in func :
        if i == 'D' :
            cnt += 1
    if cnt > l :
        print("error")
        continue

    arr = deque(arr)
    flag = 0
    for i in func :
        if i == 'R' :
            if flag == 0 :
                flag = 1
            else :
                flag = 0
        elif i == 'D':
            if flag == 1 :
                arr.reverse()
                flag = 0
            arr.popleft()
    print(list(arr))

end_time = time.time()
print('time: ', end_time - start_time)