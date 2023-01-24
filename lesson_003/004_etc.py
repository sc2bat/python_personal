'''
# continue
for i in range(1, 11) :
    if i == 5 :
        continue
    print(i)
'''

'''
# break
for i in range(1, 11) :
    if i == 5 :
        break
    print(i)
'''

'''
# pass
for i in range(1, 11) :
    if i == 5 :
        pass
    print(i)
'''

# 비워두기 python 은 제어문 내용을 비워둘 수 없음 pass 사용
n = int(input('n : '))
if n > 0 :
    #
    pass
else :
    #
    print('else')