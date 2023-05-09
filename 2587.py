
num_list = []
answer = 0
for i in range(5):
    n = int(input())
    answer += n
    num_list.append(n)
num_list.sort()

print(answer//5)
print(num_list[2])

