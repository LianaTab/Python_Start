'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no

'''

n = int(input('Введите размер n шоколадки: '))
m = int(input('Введите размер m шоколадки: '))
k = int(input('Сколько долек нужно отломить? '))

choko = int(n * m)
if (k%2 == 0) and (k < choko):
    print('YES')
else:
    print('NO')
