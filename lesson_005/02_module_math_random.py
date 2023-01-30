import math

math.ceil(2.1) # 올림
math.floor(2.1) # 내림
math.factorial(10) # 팩토리얼
math.sqrt(4) # 루트
math.pi # 원주율

'''
print(math.ceil(2.1)) # 3
print(math.floor(2.1)) # 2
print(math.factorial(10)) # 3628800
print(math.sqrt(4)) # 2.0
print(math.pi) # 3.141592653589793
'''

import random

random.randint(1, 5) # 범위 내 정수 랜덤값 생성
random.random() # 0 <= ?? < 1 랜덤값 생성

li = ['a', 'b', 'c', 'd', 'e']
random.choice(li) # 리스트 값 중 하나 랜덤 뽑기
random.sample(li, 3) # 리스트에서 랜덤 n 개 뽑기
random.shuffle(li) # 리스트 순서 랜덤 섞기

print(random.sample(li, 3))

