# tuple 만들면 값을 변경할 수 없음

# Tuple 만들기
'''
tuA = ()
tuA = tuple()
'''

'''
# Tuple index
tuB = ('a', 'b', 'c')
print(tuB) # ('a', 'b', 'c')
for i in range(len(tuB)) :
    print('tuB i : ', tuB[i])
'''

# Tuple 활용
'''
tuC = ('a', 'b', 'c', 'd')
print(tuC.index('c'))   # 2 
print('d' in tuC)       # True
print(len(tuC))         # 4
print(tuC.count('d'))   # 1
'''

# 변수 할당
'''
numA = (5, 6, 10)
n1, n2, n3 = numA
print('n1 : ', n1, ' n2 : ', n2, ' n3 : ', n3) # n1 :  5  n2 :  6  n3 :  10
'''

# 값 교환하기
'''
a = 'hello'
b = 'world'
print('a : ', a, ' b : ', b) # a :  hello  b :  world
(a, b) = (b, a)
print('a : ', a, ' b : ', b) # a :  world  b :  hello
'''

listD = ['a', 'b', 'c']
tupleD = ('a', 'b', 'c')
# List to Tuple
print(type(tuple(listD))) # <class 'tuple'>
print(type(list(tupleD))) # <class 'list'>



