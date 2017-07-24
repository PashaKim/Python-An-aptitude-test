"""
Скрипт, который принимает список строк, содержащий целые числа и слова и возвращает упорядоченную версию списка. 
 В упорядоченной версии позиции чисела и строки сохраняються.

"""
your_input = input('Ваш список: ')
numbers = [int(n) for n in your_input.split() if n.isdigit()]
numbers.sort(key=int) #Сортировка чисел
words = [str(s) for s in your_input.split() if s.isalpha()]
words.sort() #Сортировка слов)
list = your_input.split(" ")

intIndex = 0 #Индексы на замену
strIndex = 0

for index, item in enumerate(list):
    if item.isdigit(): # Если число, меняю из списка numbers
        list[index] = numbers[intIndex]
        intIndex+=1

    elif item.isalpha():
        list[index] = words[strIndex]
        strIndex +=1

print('Отсортированный список: ', list)
input("Press Enter to continue...")



