arr = []
for i in range(9):
	arr.append(int(input()))

arr.sort()
sum_arr = sum(arr)
big1, big2 = 0, 0

for i in range(8):
	for j in range(i + 1, 9):
		if sum_arr - (arr[i] + arr[j]) == 100:
			big1 = arr[i]
			big2 = arr[j]


arr.remove(big1)
arr.remove(big2)
arr.sort()

for i in arr:
    print(i)
