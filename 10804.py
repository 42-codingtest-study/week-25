# 0x01강_카드 역배치

import sys

input = sys.stdin.readline

c = [ i for i in range(21)]
for _ in range(10) :
    a, b = map(int, input().split())

    for i in range((b - a + 1) // 2) :
        tmp = c[b - i]
        c[b - i] = c[a + i]
        c[a + i] = tmp

for i in c[1:] :
    print(i, end = ' ')