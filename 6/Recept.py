"""
Функция, которая принимает словарь с рецептом и словарь с количеством доступных ингридиентов 
и возвращает количество порций, которые мы можем приготовить.

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
count(recipe, available) -> 2

 Python3.6.1
"""

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(recipe)
print(available)

def cook(recipe,available):
    d = dict((k, float(available[k]) // recipe[k]) for k in recipe)
    key_min = min(d.keys(), key=(lambda k: d[k]))
    print(d[key_min])

cook(recipe, available)
