# 문자열 인덱스

'''
text = 'abc'

print(text[0]) # text[-3] == text[0]
print(text[1]) # text[-2] == text[1]
print(text[2]) # text[-1] == text[2]
'''

# 문자열 슬라이스
text = 'abcde fgh ijk'
print(text)
'''
# text[처음시작하는 인덱스 : 끝내고싶은 문자의 인덱스 + 1]
print(text[2:5]) # cde
print(text[1:8]) # bcde fg
print(text[-5:-1]) # h ij   
print(text[5:]) #  fgh ijk
print(text[:5]) # abcde
print(text[:]) # abcde fgh ijk
'''
# text[처음시작하는 인덱스 : 끝내고싶은 문자의 인덱스 + 1 : 문자의 간격]
print(text[1:7:2]) # bd
print(text[7:1:-1]) # gf edc * 간격이 음수이면 반대로 값을 넣어줘야함 진행방향이 반대가 되는 것





