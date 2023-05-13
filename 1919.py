# 0x03강_애너그램 만들기

a = input()
b = input()

for s in a :
    if s in b :
        b = b.replace(s, '', 1)
        a = a.replace(s, '', 1)

sum = len(a) + len(b)
print(sum)