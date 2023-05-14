import sys
from collections import deque
import copy

n, m = map(int,sys.stdin.readline().split())
graph = []
for _ in range (n) :
    graph.append(list(map(int,sys.stdin.readline().split())))

# 상하좌우 문제는 dx, dy 쓰기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global max_safe;
    queue = deque()
    tmp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and ny < n and nx < m :
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = 2
                    queue.append((ny,nx))
    result = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0 :
                result += 1
    max_safe = max(result,max_safe)

def build(cnt) :
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 :
                graph[i][j] = 1
                build(cnt + 1)
                graph[i][j] = 0

max_safe = 0
build(0)
print(max_safe)