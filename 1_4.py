# 시간복잡도 : O(logN)
import math as m

n = int(input())
ans = 1
while 2 * ans <= n :
    ans *= 2
print (ans)
