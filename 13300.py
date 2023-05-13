# 0x03강_방 배정
# 입력을 받을 때마다 리스트에 따로 학년별 인원 수 체크하기

student_num, k = map(int, input().split())
woman = [0] * 1000
man = [0] * 1000

for j in range(student_num) :
    check, grade = map(int, input().split())
    if check == 0 :
        woman[grade] += 1
    else :
        man[grade] += 1

for j in range(1, 7) :
    if woman[j] % k == 0 :
        woman[j] = woman[j] // k
    else :
        woman[j] = (woman[j] // k) + 1
    
    if man[j] % k == 0 :
        man[j] = man[j] // k
    else :
        man[j] = (man[j] // k) + 1

print(sum(woman) + sum(man))