# Списки
## створення списків - пустий і зі значеннями
blank_list = []
big_list = [7, 336, 61, "--==--", 'spam', 'dev', 1.23]
# індексація, зрізи

## порівняння списків
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3, 4]
a < c
## вилучення значень
big_list.pop()
## методи списків
# додавання у список
big_list.append(4)
big_list.extend([5,6,7])
big_list.insert(1, "223")
# пошук, перевірка значень
value = 61
big_list.index(value)
big_list.count(value)
# впорядкування даних
big_list.sort()  #['abc', 'ABD', 'aBe']
big_list.reverse()
# зміни
big_list.copy()
big_list.clear()

# comprehensions and List Iteration
small_list = [x**2 for x in range(5)]

# Словники
## створення словників
blank_dict =  {}
small_dict = {'name':'Mary', 'second': 'Ann', 'age': 18}
big_dict= {'user': {'name':'Bob', 'second': 'Hand', 'age': 40},
           'is_blocked': False,
           'salary': 10000}

## додавання значень в словник
## методи словника
big_dict.keys()
big_dict.values()
big_dict.items()
big_dict.copy()
big_dict.clear()
big_dict.update({"key":"value"})
big_dict.popitem("key")
big_dict.get("key", "default")
big_dict.pop("key", "default")


# Сети (набори)

## перетворення в набір

## операції з наборами

# Tuples

