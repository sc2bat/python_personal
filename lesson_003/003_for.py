# range()
# 범위 또는 증감 값ㄷ을 정하면 
# 규칙적인 수들의 집합으로 만들어주는 함수

'''
range(a) ==> 0 ~ a - 1

range(a, b) ==> a ~ b - 1

range(a, b, c) ==> a ~ b - 1, c 씩 증가

# a, b, c 는 int(정수) 만 가능

for i in range(20, 100, 10):
    print('i : ', i)
i :  20
i :  30
i :  40
i :  50
i :  60
i :  70
i :  80
i :  90

'''
'''
range(5)
list(range(0, 5)) # 0, 1, 2, 3, 4
list(range(1, 11)) # 1,2,3,4,5,6,7,8,9,10
list(range(3, 10, 3)) # 3, 6, 9
list(range(5, 0, -1)) # 5,4,3,2,1
list(range(10, -11, -5)) # 10, 5, 0, -5, -10
'''

'''
# for 
for i in range(10) :
    print(i)
'''

#n = int(input('n : '))
'''
# 1 ~ n 까지 출력
for i in range(1, n) :
    print('i : ', i)
'''
'''
# a ~ b 까지 출력
#a = int(input('a : '))
#b = int(input('b : '))
a, b = map(int, input('a, b : ').split())
for i in range(a, b + 1) :
    print('a ~ b : ', i)
'''

'''
# n ~ 0 까지 출력
for i in range(n, -1, -1) :
    print('i : ', i)
'''







