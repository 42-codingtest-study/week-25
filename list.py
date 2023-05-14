word = ['y', 'a', 'x']

word.sort()
print(word[0])

# dict
research = ['aaaba', 'afbbaa', 'abbbbfcf']
N = 2
K = 2

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
    dic[word[i]] = i

print(dic)
print(dic.pop('c'))
print(dic)

dic2 = {'k' : 5, 'a' : 100}
dic.update(dic2)
print(dic)