from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

# print(dq)
count = 0
for num in num_list:
	while True:
		if dq[0] == num:
			dq.popleft()
			break
		else:
			if dq.index(num) <= len(dq) // 2:
				print("index" , dq.index(num), dq)
				dq.rotate(-1)
				count+=1
			else:
				print("index" , dq.index(num), dq)
				dq.rotate(1)
				count+=1
print(count)


