"""
Написать скрипт, который принимает строку, состоящую из слов, разделённых символом _ или -
и возвращает строку в camel case. При этом регистр первого символа менять не нужно.


the_phantom_menace -> thePhantomMenace
The-Phantom-Menace -> ThePhantomMenace
 
"""

your_input = str(input('Генератор СamelСase, введите вашу строку: '))
d = {'-': '', '_':''}
t = list(your_input) # Первая буква
for x,y in d.items():
    your_input = your_input.title().replace(x, y)
l = list(your_input)
l.pop(0)
strl = ''.join(l)
print(t[0]+strl)
