# 시간복잡도 : O(N)
def func1(num) :
    ans = 0
    for i in range (1, num + 1):
        if i % 3 == 0 or i % 5 == 0 :
            ans += i
    return ans

n = int(input())
print (func1(n))
