"""
Есть последовательность чисел, содержащая как минимум 3 элемента, но которая может быть очень большой. 
Элементы являются целыми числами, которые либо все чётные, либо все нечётные, за исключением одного.
Cкрипт, выводит это единственное отличающееся число.
[0 8 2 50 13 6 34] -> 13
"""

chisla = [0, 8, 2, 50, 13, 6, 34]
#chisla = [1, 3, 5, 31, 3, 6, 1]
proverka = []
proverka2 =[]
for i in chisla:
    if i%2 == 0:#Четное
        proverka.append(i)
        if len(proverka) > 1:
            continue
        elif len(proverka) == 1:
            print(i)

    else:
        proverka2.append(i)
        if len(proverka2) > 1:
            continue
        elif len(proverka2) == 1:
            print(i)




input("Press Enter to continue...")
