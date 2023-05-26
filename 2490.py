# first_list = list(map(int,input().split()))
# second_list = list(map(int,input().split()))
# third_list = list(map(int,input().split()))

for c in range(3):
    lst = list(map(int,input().split()))
    count = 0
    for i in lst:
        if i == 0:
            count += 1

    if count == 0:
        print("E")
    elif count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")
