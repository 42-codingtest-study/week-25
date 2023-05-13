# 0x01강_핸드폰 요금

import sys

input = sys.stdin.readline

n = int(input())
Y = 0
M = 0
num = []
num = list(map(int, input().split()))

for i in range(n) :
    if num[i] % 30 == 0 :
        Y += (10 * (num[i] // 30) + 10)
    else :
        Y += (10 * (num[i] // 30) + 10)
    if num[i] % 60 == 0 :
        M += (15 * (num[i] // 60) + 15)
    else :
        M += (15 * (num[i] // 60) + 15)

if Y > M :
    print("M", M)
elif Y < M :
    print("Y", Y)
elif Y == M :
    print("Y", "M", Y)