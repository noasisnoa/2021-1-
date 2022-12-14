# -*- coding: utf-8 -*-
"""08 Python function - part 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13KRog0Kab3E6R0bEnGjfA7BlcDgogS45
"""

a = 10
b = 20

a + b

"""## 함수란

- 어떤한 기능을 사용할 때 마다 코드를 작성하는 것이 아닌

함수가 사용되어지는 과정

- 함수가 호출되면 실행의 흐름이 호출자(callerr)에서 함수(callee)로 변경된다.
"""

def div(x, y):
    print(f'나누기 수행 : {x} / {y}') # f
    return x / y

print('Hello')
c = div(10, 3)
print(c)

def a(x = 5, y = 0 ):
    print(f'곱하기 수행 : {x} * {y}')
    return x * y

def b(x = 5, y = 0):
    print(f'더하기 수행 : {x} + {y}')
    return x + y

def c(x = 5, y = 0):
    print(f'빼기 수행 : {x} - {y}')
    return x - y

print('Hello')
c = a()  # (,4) '공백 ,'은 시작을 할 수 없다.
print(c)

"""함수의 네이밍

- 함수의 이름으로부터 기능이 명시
- 함수 이름도 변수의 이름처럼 항상 의미를 파악할 수 있는 이름으로 지을 것
"""

def a():
    print('haha')
    
def print_haha():
    print('haha')
    
print_haha() # 함수의 print 값을 가지고 오기 위해서는 함수의 이름하고 ()해야한다.

#def b(x, y):
#    print(f'{x} + {y}')

def print_x_y(x, y):
    print(f'{x} + {y}')
    return x + y

c = print_x_y(10, 3)
print(c)

"""변수 이름은 명사 처럼 지어주는 것이 좋고, 함수 이름은 문장처럼 지어주는 것이 좋다.

Parameter(argument)
- 함수에 전달되는 입력값
"""

def sub(x, y):
    print(f'빼기 수행 : {x} - {y}')
    return x - y

a = sub(10, 7)
print(a)

b = sub(10, 0.6)
print(b)

"""default parameter(기본 인자 설정)

- 함수의 파라미터에 기본값 지정 가능
- 파라미터를 전달하지 않으면, 사전에 지정한 값으로 자동 설정됨
"""

def print_param(x, y=10, z=5):
    print(f'x : {x} / y : {y} / z :{z}')
    
print_param(1, 2, 3,)
print_param(1) # x에만 값을 전달
print_param(1, 100)

"""함수란?

- 어떠한 기능을 사용할 때 마다 코드를 작성하는 것이 아닌,

multiple return(복수 개의 값을 리턴)
-tuple로 자동 변환 되어서 값을 리턴

! 클래스로 사칙연산 만들어보세요
"""

class Math:
    
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiplay(x, y):
        return x * y
    
    def division(x, y):
        return x / y

print(Math.add(10, 4))
print(Math.subtract(10, 4))
print(Math.multiplay(10, 4))
print(Math.division(10, 4))

"""! 강아지 객체가 만들어짐"""

class Animal:
    
    def __init__(self, name):
        print('동물 객체가 만들어짐')
        self.name = name
        
    def eat(self, food):
        print('{}가 {}를 먹었습니다.'.format(self.name, food))
        
class Dog(Animal):           ### 이힝 여기가 이해가지 않아요 왜 Animal 이 왜 들어가기?/ 두 개가 들어갈 수 없다.
    
    def __init__(self, name):
        print('강아지 객체가 만들어짐')
        self.name = name

myDog = Dog('까망이')
myDog.eat('사료')

class person:
    def __init__(self, ) # __init__ 초기화

my.Dog = Dog('까망이')
my.Dog.eat('사료')

"""! method의 정의, 그래프 그려서 80에서 내려갈 때 80까지만 좋은 거구나.., 기록하기 중요해요

! 다차원 행렬 자료 구조,

Numpy
- Numpy 파이썬의 수치 해석용 라이러리 이다
- 실질적으로 다차원

! 슬라이싱 위치 알기

ndarry 클래스
"""