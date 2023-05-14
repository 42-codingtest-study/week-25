import sys
from collections import deque

city, road, distance, start = map(int,sys.stdin.readline().split())
# 최단거리 배열 만듬(지도)
answer = [-1] * (city+1)
answer[start] = 0

# 그래프 틀 만듬
graph = [[]for _ in range (city + 1)]

# 그래프 채움
for _ in range(road):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

def bfs(graph, start, answer):
    queue = deque([start])
    while queue:
        v= queue.popleft()
        for w in graph[v]:
            if answer[w] == -1:
                answer[w] = answer[v] + 1
                queue.append(w)

bfs(graph, start, answer)

if answer.count(distance) == 0 :
    print(-1)
else :
    for i in range(1, city + 1):
        if answer[i] == distance:
            print(i)