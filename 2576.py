num_list = []
for i in range(7):
    num_list.append(int(input()))
# print(num_list)

res = 0
arr = []
for i in num_list:
    if i % 2 == 1:
       res += int(i)
       arr.append(i)

if res == 0:
    print(-1)
else:
	print(res)
	print(min(arr))
