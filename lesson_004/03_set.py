# set 만들기
'''
setA = set()
setA = {} # 사용 불가 비어있는 세트 만들기 불가
'''
# set 특징 (순서, 중복 없음)
'''
a = {2, 4, 6, 8} # {8, 2, 4, 6}
b = {2, 4, 2, 1, 2, 3} # {1, 2, 3, 4}

print(a[0]) # 순서가 없기 때문에 index 로 값을 불러올 수 없음
'''

# set 활용
'''
a = {2, 4, 6, 8} 
a.add(5)        # set add
a.remove(5)     # set delete
1 in a          # check in
len(a)          # length
sum(a)          # sum
min(a)          # min
max(a)          # max
list(a)         # set to list
tuple(a)        # set to tuple
'''

a = {1, 2, 3}
b = {2, 3, 4}
print( a & b )       # 교집합 {2, 3}
print( a | b )       # 합집합 {1, 2, 3, 4}
print( a - b )       # 차집합 {1}
print( a ^ b )       # 대칭 차집합 {1, 4}





