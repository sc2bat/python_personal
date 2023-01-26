# 문자를 입력받아 공백 기준 자르기
'''
listA = input('write String : ').split()
print(listA)
# write String : asdf
# ['asdf']
# write String : as bvb ww
# ['as', 'bvb', 'ww']
'''

# 문자를 입력받아 전체 자르기
'''
listB = list(input('write String : '))
print(listB)
# write String : asdfasdfasdf
# ['a', 's', 'd', 'f', 'a', 's', 'd', 'f', 'a', 's', 'd', 'f']
'''

# 숫자를 여러개 입력받기
'''
listC = list()
listC.append(int(input('write int : ')))
listC.append(int(input('write int : ')))
listC.append(int(input('write int : ')))
print(listC)
# write int : 33
# write int : 22
# write int : 111
# [33, 22, 111]
'''

# 숫자를 여러개 입력받기 2
'''
listD = list(map(int, input('write Integer : ').split()))
# a = input('write Integer : ').split()
# b = map(int, a)
# c = list(b)
print(listD)
# write Integer : 33 11445 6666
# [33, 11445, 6666]
'''

# 합, 평균, 최소값, 최대값, 중간값
numA = list(map(int, input('write Integer : ').split()))
numA.sort()     # 정렬 # [11, 23, 44]
print('sum : ', sum(numA))                  # sum :  78
print('avarage : ', sum(numA) / len(numA))  # avarage :  26.0
print('min : ', numA[0])                    # min :  11
print('max : ', numA[len(numA) - 1])        # max :  44
print('middle value : ', numA[len(numA) // 2]) # middle value :  23