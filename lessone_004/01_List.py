# list 생성
# list index
# list 활용

# 리스트 만들기
listA = []
listA = list()

# list index
'''
listB = ['a', 'b', 'c']
print(listB[0])
print(listB[1])
print(listB[2])
listB[2] = 'd'
print(listB[2])
'''

# list 활용
'''
listC = ['a', 'b', 'c', 'd', 'e']
print(listC.index('c')) # find index
listC.append('c')       # add 1
listC.insert(0, 'aa')   # add 2
listC.remove('aa')      # delete 1
del listC[2]            # delete 2
print(len(listC))       # length
print(listC.count('a')) # counting
'''

'''
num = [1, 2, 3, 4, 5, 6, 7, 8]
print('sum : ', sum(num)) # sum :  36
print('min : ', min(num)) # min :  1
print('max : ', max(num)) # max :  8

num.reverse() # reverse list
for i in range(len(num)) :
    print('reverse i : ', num[i])

num.sort() # 오름차순 정렬
for i in range(len(num)) :
    print('sort i : ', num[i])
    
num.sort(reverse = True) # 내림차순 정렬
for i in range(len(num)) :
    print('sort reverse = True i : ', num[i])
'''







