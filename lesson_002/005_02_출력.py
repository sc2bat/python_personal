'''
# 1. 출력 지정 : format(a, b, c, ...)
text = 'abced {} {}'
print(text.format('ABC',123)) # abced ABC 123
'''

'''
# 2. 대체하기 : replace(a, b)
text = 'abcde ABC DEF'
print(text.replace('ABC', 'KKK')) # abcde KKK DEF
'''

'''
# 3. 자르기 : split(a)
text = 'abcde A/B/C A.B.C'
a, b, c = text.split('.')
print(a) #abcde A/B/C A
print(b) # B 
print(c) # C  

a, b, c = text.split('/')
print(a) # abcde A
print(b) # B    
print(c) # C A.B.C
'''
'''
# 4. 합치기 : a.join()
text = 'abcde'
print('/'.join(text)) # a/b/c/d/e
print('12'.join(text)) # a12b12c12d12e
'''

'''
# 5. 개수 확인하기 : count(a)
text = 'abcde ABC ABC' 
print(text.count('a')) # 1
print(text.count('A')) # 2
print(text.count('1')) # 0
'''
'''
# 6. 제거하기 : strip(a) / lstrip(a) / rstrip(a)
text = '**abcde****'
print(text.strip('*')) # abcde
print(text.lstrip('*')) # abcde****
print(text.rstrip('*')) # **abcde
'''
'''
# 7. 인덱스 찾기 : find(a) / rfind(a) /index(a) /rindex(a)
text = 'ABC ABC'
print(text.find('A')) # 0
print(text.rfind('A')) # 4
print(text.index('A')) # 0
print(text.rindex('A')) # 4
'''
'''
# 8. 확인하기 : 
# isalpha() 알파벳인가
# isdigit() 숫자인가
# isalnum() 알파벳 + 숫자인가
# isupper() / islower() 대문자인가 소문자인가
# result True or False
text1 = 'ABCabc123'
text2 = '123'
text3 = 'ABC'
text4 = 'abc'

print(text1.isalpha()) # False
print(text1.isdigit()) # False
print(text1.isalnum()) # True
print(text1.isupper()) # False
print(text1.islower()) # False
'''

# 9 대/소문자 만들기 : upper() /lower()
text = 'ABCabc'
print(text.upper()) # ABCABC
print(text.lower()) # abcabc

# 10. 0 채우기  : zfill()
y = '2020'
m = '3'
d = '1'
print(y.zfill(4)) # 2020 
print(m.zfill(2)) # 03
print(d.zfill(3)) # 001








