# for 문으로 list append
'''
listA = []

for i in range(5) :
    listA.append(int(input('write int : ')))

print(listA)

# write int : 1
# write int : 23
# write int : 3
# write int : 4
# write int : 5
# [1, 23, 3, 4, 5]
'''

# for 문으로 list 값 출력
'''
listB = [1, 23, 3, 4, 5]
for i in range(len(listB)) :
    print(listB[i])
'''

'''
listC = [1, 23, 3, 4, 5]
for i in listC :
    print(i)
'''

# if 문 추가
'''
listD = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(listD)) :
    if i % 2 == 0 :
        print(listD[i])

print('=========')

for i in listD :
    if i % 2 == 0 :
        print(i)
'''

# 리스트 분리하기
'''
listE = list(input('write String : '))

upperList = []
lowerList = []

for i in listE :
    if i.isupper():
        upperList.append(i)
    elif i.islower() :
        lowerList.append(i)

print('upperList : ', upperList)
print('=========')
print('lowerList : ', lowerList)

write String : asdfzASDFAWEF
upperList :  ['A', 'S', 'D', 'F', 'A', 'W', 'E', 'F']
=========
lowerList :  ['a', 's', 'd', 'f', 'z']
'''












