# sk back-end 코테 2번

# research = ['aaaba', 'afbbaa', 'abbbbfcf'] 날짜별 검색어
research = list(input().split())

# 검색 N번 이상
N = int(input())
# 연속 K일 이상
K = int(input())

word = set()
for day in research :
    re = list(day)
    word.update(re)

graph = [[ 0 for i in range (len(research) + 1)] for _ in range (len(word) + 1)]
word = list(word)
word.sort()

for i in range(1,len(research) + 1):
    graph[0][i] = str(i) + ' days'

graph[0][0] = 'research'
dic = {}
for i in range (0, len(word)) :
    graph[i + 1][0] = word[i]
    dic[word[i]] = 0

for i in range(0, len(research)) :
    re = list(research[i])
    for j in range(len(re)):
        dic[re[j]] += 1
    check = list(dic.values())
    for k in range(len(word)):
        graph[k + 1][i + 1] = check[k]
    for j in range(len(re)):
        dic[re[j]] = 0 

result = []

for i in range(0, len(word)) :
    cnt = 0
    wow = 0
    for j in range (0, len(research)) :
        if graph[i+1][j+1] >= N :
            cnt += 1
        else :
            cnt = 0
        wow = max(wow, cnt)
    if wow >= K :
        result.append(graph[i+1][0])


print(result[0])