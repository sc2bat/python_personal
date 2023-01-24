# if + if
'''
age = int(input('age ? '))

if age <= 7 :
    print('a')
elif age <= 19 :
    print('b')
    if age <= 13 :
        print('b a')
    elif age <= 16 :
        print('b b')
    else :
        print('b c')
else :
    print('c')
'''

# for + if
'''
n = int(input('n : '))
for i in range(1, n + 1) :
    if i % 3 == 0 :
        print('X')
    else : 
        print('i : ', i)
'''

# while + if
'''
num1 = 0
num2 = int(input('n : '))
while True :
    num1 = num1 + 1
    print(num1)
    if num1 == num2 :
        break
'''

# for + for
'''
for i in range(1, 5) :
    for j in range(1, 5) :
        print(i , j)
'''



