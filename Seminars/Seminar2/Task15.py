"""
15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для 
тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же 
выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит 
N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса 
соответствующего арбуза
Input: 5 -> 5 1 6 5 9 Output: 1 9

"""

wm_count = int(input())
max_wm = int(input('wm_0--> '))
max_wm_i = 0
min_wm = max_wm
min_wm_i = 0
wms = []

for i in range(1, wm_count):
    wm = int(input(f'wm_{i}--> '))
    if wm > max_wm:
        max_wm = wm
        max_wm_i = i
    if wm < min_wm:
        min_wm = wm
        min_wm_i = i

print(max_wm, min_wm)


"""
print(max(wms))
print(min(wms))
"""
"""
# Input: 5 -> 5 1 6 5 9
# Output: 1_1 4_9


wm_count = int(input())
max_wm = int(input('wm_0--> '))
max_wm_i = 0
min_wm = max_wm
min_wm_i = 0

for i in range(1, wm_count):
wm = int(input(f'wm_{i}--> '))
if wm > max_wm:
max_wm = wm
max_wm_i = i
if wm < min_wm:
min_wm = wm
min_wm_i = i

print((min_wm, min_wm_i), (max_wm, max_wm_i))

"""