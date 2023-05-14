#
# 10808
# 알파벳 개수
# https://www.acmicpc.net/problem/10808

import sys
input = sys.stdin.readline

alphbet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = [0] * 26

s = input()

for i in s:
    for j in alphbet:
        if i == j:
            count[alphbet.index(j)] += 1

for i in count:
    print(i, end=' ')