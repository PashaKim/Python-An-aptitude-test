"""
Написать функцию, принимающую последовательность словарей, содержащих имена и возвращающую имена через запятую,
 кроме последнего, присоединённого через амперсанд.

[{'name': 'John'}, {'name': 'Jack'}, {'name': 'Joe'}] -> 'John, Jack & Joe'
[{'name': 'John'}, {'name': 'Jack'}] -> 'John & Jack'
[{'name': 'John'}] -> 'John'

 
"""

name1 = {'name':'Jhon'}
name2 = {'name':'Jack'}
name3 = {'name':'Joe'}
names = [name1, name2, name3]
print(names)

def dictionary_name(names):
    list_name = []
    for n in names:
        i = list(n.values())
        list_name.append(i)
    flat_list = [item for sublist in list_name for item in sublist]
    last = '& ' + flat_list[-1]  # Вывод последнего имени и амперсанта
    flat_list.pop(-1)  # Удаление последнего имени
    for index, item in enumerate(flat_list):
        print(flat_list[index], end=" "),  # чтоб в одну строчку было
    print(last)

dictionary_name(names)







#input("Press Enter to continue...")


