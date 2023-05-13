# 0x03강_두 수의 합

import sys

n = int(input())
n2 = sorted(list(map(int, sys.stdin.readline().split())))
a = int(input())
ans = 0
left, right = 0, n - 1

while left < right :
    tmp = n2[left] + n2[right]
    if tmp == a :
        ans += 1
        left += 1
    elif tmp < a :
        left += 1
    else :
        right -= 1

print(ans)