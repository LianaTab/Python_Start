'''
В некоторой школе решили набрать три новых математических 
класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. Известно количество 
учащихся в каждом из трех классов. Выведите наименьшее число парт, 
которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
'''

class_1 = int(input('--> '))
class_2 = int(input('--> '))
class_3 = int(input('--> '))

class_1 += 1
class_2 += 1
class_3 += 1

result = (class_1//2) + (class_2//2) + (class_3//2)

print(result)

# print(f'Нам нужно парт: {(class_1//2) + (class_2//2) + (class_3//2)}')