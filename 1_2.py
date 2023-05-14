# 시간복잡도 : O(N^2)
n = int(input())
arr = list(map(int, input().split()))

def func2(arr, n) :
    for i in range(0, len(arr)) :
        for j in range(i + 1, len(arr)) :
            if arr[i] + arr[j] == 100 :
                return 1
    return 0

print(func2(arr, n))