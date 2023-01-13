# map split

#strA = 'qwer qq we r'
#print(strA.split())
'''
vDate = input('날짜 입력 yyyy.mm.dd')
y, m, d = vDate.split('.')
print(vDate, y, m, d)
'''

# map(함수, 집합 형태 -iterable 객체)
#a, b, c = map(int, ['1', '2', '3'])
#print(a, b, c)
'''
vStr = input('a, b, c 값 입력')
vStr = vStr.split()
a, b, c = map(int, vStr)
print(vStr, a, b, c)
'''
# end = '' 줄바꿈 제거
'''
x = 'qwer'
print(x, end='')
print(x, end='')
print(x, end='')
'''

# .format() 순차적으로 {} 에 기입됨
'''
x = 1
y = 2
print('{}과 {}의 합은 {}이다.'.format(x, y, x + y))
'''

# 반올림 round(a)
# 절대값 abs(a)
# 제곱 pow(a, b)
# 나눔셈 divmod(a, b)
# 최대값 max(a, b, c , d ...)
# 최소값 min(a, b, c, d ..)
# 합 sum(집합 형태 : Iterable)
intlist = [1, 2, 3, 4, 5, 11]
print(sum(intlist))















