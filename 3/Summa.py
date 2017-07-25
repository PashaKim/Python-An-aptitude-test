"""
Скрипт, который составляет из списка положительных целых чисел максимально возможное число.

[70 8 20 1 13] -> 87020131

Python3.6.1
"""

lis = [70, 8, 20, 1, 13]
lis.sort(key=str, reverse=True) # Сортируем от большего к меньшему
print(lis)
lis = list(map(str, lis)) # Делаю текстом
number =int(''.join(lis))
print(number)

input("Press Enter to continue...")
