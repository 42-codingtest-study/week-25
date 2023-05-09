# 0x01강_윷놀이

for i in range(3) :
    k = list(map(int, input().split()))
    if k.count(0) == 1:
        print("A")
    elif k.count(0) == 2:
        print("B")
    elif k.count(0) == 3:
        print("C")
    elif k.count(0) == 4:
        print("D")
    else :
        print("E")