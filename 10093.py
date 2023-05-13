# 0x01강_숫자

a, b = map(int, input().split())
num1 = min(a, b)
num2 = max(a, b)
cnt = num2 - num1 - 1

if num2 - num1 <= 1 :
    cnt = 0

print(cnt)
arr = [i for i in range(num1 + 1, num2)]
print(*arr, end='')