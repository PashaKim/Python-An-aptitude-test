"""
Скрипт, который принимает строку, состоящую из слов, разделённых символом _ или -
и возвращает строку в camel case. При этом регистр первого символа менять не нужно.


the_phantom_menace -> thePhantomMenace
The-Phantom-Menace -> ThePhantomMenace
 
 Python3.6.1
"""

your_input = str(input('Генератор СamelСase, введите вашу строку: '))
d = {'-': '', '_':''}
t = your_input[0] # Первая буква
word = your_input.title()
for x,y in d.items():
    word = word.replace(x, y)
lst = list(word)
lst.pop(0)
strl = ''.join(lst)
print(t+strl)
