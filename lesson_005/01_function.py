# function

# define function
def aa() :
    print('function aa() ')

def bb(x) :
    for i in range(x) :
        print('bb(x)', i)

def cc() :
    n = int(input('n : '))
    print(n * 2)
    return n * 2

def dd(x, y) :
    print(x * y)
    return x * y

# 함수 호출하기
re1 = aa() # function aa() 
re2 = bb(3)
# bb(x) 0
# bb(x) 1
# bb(x) 2
re3 = cc() # n : 33 # 66
re4 = dd(2, 5) # 10


