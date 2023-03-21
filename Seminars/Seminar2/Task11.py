'''
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи 
оно является, то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите число -1.

Input: 5

Output: 6

'''

"""
A = int(input('Введите число: '))
fib1 = 0
fib2 = 1
n = 2
while fib2 <= A:
    if fib2 == A:
        print(n)
        break
    fib1, fib2 = fib2, fib1 + fib2
    n += 1
else:
    print(-1)
"""

"""
A = int(input('Введите число: '))
fib1 = 0
fib2 = 1
n = 2
flag = True
while fib2 <= A:
    if fib2 == A:
        print(n)
        flag = False
    fib1, fib2 = fib2, fib1 + fib2
    n += 1
if flag:
    print(-1)

"""

A = int(input('Введите число: '))
fib1 = 0
fib2 = 1
n = 2
while fib2 < A:
    fib1, fib2 = fib2, fib1 + fib2
    n += 1
if fib2 == A:
    print(n)
else:
    print(-1)