# 0x01강_숫자의 개수

import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

total = list(str(a * b * c))

for i in range(10) :
    print(total.count(str(i)))