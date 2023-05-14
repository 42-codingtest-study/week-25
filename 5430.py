import sys
input = sys.stdin.readline

t = int(input())

for _ in range (t):
    func = list(map(str, input().rstrip()))
    l = int(input().rstrip())
    in_arr = list(map(str, input().rstrip()))
    if len(in_arr) == 2 : 
        print("error")
        continue
    del in_arr[0]
    del in_arr[len(in_arr)-1]
    arr_str = ''.join(in_arr)
    arr = list(map(int, arr_str.split(',')))
    cnt = 0
    
    for i in range(0, len(func)) :
        if func[i] == 'D' :
            cnt += 1
    if cnt > l :
        print("error")
        continue
    flag = 0
    for i in range(0, len(func)) :
        if func[i] == 'R' :
            if flag == 0 :
                flag = 1
            else :
                flag = 0
        elif func[i] == 'D':
            if flag == 1 :
                arr.reverse()
                flag = 0
            del arr[0]
    print(arr)