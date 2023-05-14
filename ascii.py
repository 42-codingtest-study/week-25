arr = list(map(str, input().split()))

print('A : ', ord('A'), '  Z : ', ord('Z'))
print('a : ', ord('a'), '  z : ', ord('z'))

for i in arr :
    print(ord(i) - 97)

print('65 : ', chr(65), '  90 : ', chr(90))
print('97 : ', chr(97), '  122 : ', chr(122))

alpha = []
for i in range (97, 123) :
    alpha.append(chr(i))

print(alpha[3].isalpha())