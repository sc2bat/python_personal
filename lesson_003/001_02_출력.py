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











