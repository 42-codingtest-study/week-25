# 0x03강_방 번호

n = int(input())
c = [0] * 10

for i in str(n) :
    if i == "9" or i == "6" :
        if c[6] == c[9] :
            c[6] += 1
        else :
            c[9] += 1
    else :
        c[int(i)] += 1

print(max(c))