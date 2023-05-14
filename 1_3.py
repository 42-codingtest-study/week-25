# 시간복잡도 : sqrt함수복잡도 만큼
import math

n = int(input())
a = math.sqrt(n)

if a - round(a) :
    print(0)
else :
    print(1)