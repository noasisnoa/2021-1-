# -*- coding: utf-8 -*-
"""2021.05.16 수업 퀴즈.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rkt3kxx_t0-PcmUYgT2jXpC19GV_ios1
"""

a = int(input('A:'))
b = int(input('B:'))

print(a + b)
print(a - b)
print(a * b)
print(a / b)

while 1 :
    st1, st2, st3 = input('숫자를 입력하세요').split()

    a = int(st1)
    b = st2
    c = int(st3)
    if b == '+':
        print(a + c)
    
    elif b == '-':
        print(a - c)
        
    elif b == '/':
        print(a / c)
    elif b == '*':
        print(a * c)
    else:
        break