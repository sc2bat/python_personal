# dic = { 키 : 값, 키 : 값, 키 : 값}

# dictionary 만들기
dicA = {}
dicB = dict()

# dictionary 특징
'''
dicC = {
    'keyC' : 'valueC'
    , 'kor' : 33
    , 'eng' : 100
    , 'mat' : 77
}

print(dicC['kor']) # 33
# dicC[0] index 가 아닌 key 값으로 
'''

# dictionary 활용
dicD = {
    'keyC' : 'valueC'
    , 'kor' : 33
    , 'eng' : 100
    , 'mat' : 77
}
'''
del dicD['mat']     # delete
dicD.claer()        # delete all
'eng' in dicD       # check by key
len(dicD)           # length
'''

dicD.keys()         # get all keys
dicD.values()       # get all values
dicD.items()        # 모든 순서쌍 얻기

print(dicD.items()) # dict_items([('keyC', 'valueC'), ('kor', 33), ('eng', 100), ('mat', 77)])
# items() 의 경우 list 또는 tuple 로 감싸더라도 내부는 tuple 형태임

# list tuple set 으로 dictionary 를 감싸게 되면 key 값만 출력됨
print(list(dicD)) # ['keyC', 'kor', 'eng', 'mat']
print(tuple(dicD)) # ('keyC', 'kor', 'eng', 'mat')
print(set(dicD)) # {'kor', 'mat', 'eng', 'keyC'} 순서 없음

# list to dictionary 짝이 맞아야 변환이 가능
listA = ['ab', 'bc', 'cd']
print(dict(listA)) # {'a': 'b', 'b': 'c', 'c': 'd'}



