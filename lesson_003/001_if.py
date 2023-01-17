# 조건이 참일 때 => 실행
# 조건이 거짓일 때 => 실행 안함

#if 조건 :
#    실행 코드

#num = int(input('숫자 하나 입력 : '))
# if
#if num > 0 :
#    print('{} 는 양수입니다.'.format(num))

# if else
'''
if num % 2 == 0 :
    print('{} 짝수'.format(num))
else :
    print('{} 홀수'.format(num))
'''

# if ~ elif
'''
age = int(input('나이 입력 : '))

if age <= 7 :
    print('{} 살 유아입니다.'.format(age))
elif age <= 19 :
    print('{} 살 청소년입니다.'.format(age))
elif age >= 20 :
    print('{} 살 성인입니다.'.format(age))
'''

# if ~ elif ~ else
text = input('알파벳 입력 : ')

if text.isupper() :
    print('{} 대문자'.format(text))
elif text.islower() :
    print('{} 소문자'.format(text))
else :
    print('대/소문자 구분 불가'.format(text))

