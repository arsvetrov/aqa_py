some_one_str = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteu sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum
"""
upper_char = "qwertyuiopasdfghjklzxcvbnm".upper()
count = 0
for i in some_one_str:
    if i in upper_char:
        count = count + 1
        #count += 1
#print(count)
print(upper_char)
upper_char = upper_char + "a"
print(some_one_str[0:5])

# Списки
## створення списків - пустий і зі значеннями
blank_list = []
big_list = [7, 336, 61, "--==--", 'spam', 'dev', 1.23]
# індексація, зрізи
print(big_list[1:4])

## порівняння списків
a = [1, 1, 3, 1]
b = [1, 3, 2]
c = [1, 2, 3, 4]
print(a > b)  # так не робити!!!!
print(a == b)
print(a != b)
print(1 in a) # True
print(7 in a) # False

## методи списків
# додавання у список
big_list.append(4)
print(big_list)
big_list[1] = 338
print(big_list)

big_list.extend([5,6,7])
print(big_list)
big_list.insert(1, "223")
print(big_list)

## вилучення значень
list_value = big_list.pop(2)
print(list_value)
print(big_list)
# пошук, перевірка значень
value = 'spam'
index = big_list.index(value)
print(index)
print(big_list.count(7))
# впорядкування даних

small_list =['abc', 'ABD', 'aBe']
number_list = [1,5,4,3,7,2]
small_list.sort()  #
number_list.sort()
print(small_list)
print(number_list)
bl = big_list.copy()

big_list.reverse()
print(big_list)
# зміни
print(bl)
big_list.clear()
print(big_list)

a = 0.1
b = 0.2
c = 0.3
print(a)
print(b)
print(c)
# comprehensions and List Iteration
small_list = [x**2 for x in range(5)]
print(small_list)

# Словники
## створення словників
blank_dict =  {}
small_dict = {'name':'Mary', 'second': 'Ann', 'age': 18}
big_dict= {'user': {'name':'Bob', 'second': 'Hand', 'age': 40},
           'is_blocked': False,
           'salary': 10000}
print(big_dict['is_blocked'])
print("*"*88)
## додавання значень в словник
## методи словника
for i in big_dict:
    print(i)
big_dict.keys()
print(big_dict.values())
print("*"*88)
for k, v in big_dict.items():
    print(k,":", v)
print("*"*88)
print(big_dict["user"]['second'])
big_dict.copy()
big_dict.clear()
big_dict["user"] = small_dict
print(big_dict["user"]['second'])
big_dict["is_blocked"] = True
print(big_dict)
big_dict.update({"user2":{'name':'Bob', 'second': 'Hand', 'age': 40}})
big_dict.update({"page": 12133})
print(big_dict)

value = big_dict.get("page", 1000)
print(value)
print(big_dict.pop("page", "default"))  #.popitem() -  видалення випадкового елемента
print(big_dict.pop("page", "default"))
# порівняння словників Dictionary Comparisons
# Example: Word Counts
text = ('this is sample text with several words '
        'this is more sample text with some different words')
# без колекцій
# з колекціями
# from collections import Counter

# Zipped key/value tuples form (ahead)
zipped = dict(zip(['a', 'b', 'c'], [1, 2, 3]))

# Сети (набори)
my_blank_set = set()
## перетворення в набір
numbers = list(range(4)) + list(range(5, 10))
set(numbers)

## операції з наборами
# порівняння
# підмножина. Еквівалентом методу issubset() є оператор <=
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a <= set_b)
# обєднання  with the '|' operator or with the set type’s 'union' method
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
# перетин 'intersection' and with the '&' operator
set_a = {1, 2, 3}
set_b = {3, 4, 5}
intersection_set = set_a & set_b  # {3}
# симетрична різниця
set_a = {1, 2, 3}
set_b = {3, 4, 5}
symmetric_difference_set = set_a ^ set_b  # {1, 2, 4, 5}


# кортежі Tuples
student_tuple = ()

# Елементи Tuple можуть бути будь-якого типу, включаючи числа, рядки, списки та інші Tuple. Наприклад:
my_tuple = ("apple", 3.14, [1, 2, 3], (4, 5, 6))

# Для доступу до елементів Tuple можна використовувати індексацію, яка починається з 0. Наприклад:
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # "banana"

# Інші корисні операції з Tuple:
# Отримання довжини Tuple:
my_tuple = (1, 2, 3)
print(len(my_tuple))  # 3

# Злиття двох Tuple:
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, "apple", "banana", "cherry")

# Перевірка наявності елемента в Tuple:
my_tuple = (1, 2, 3)
print(1 in my_tuple)  # True
print(4 in my_tuple)  # False

# Повторення Tuple:
my_tuple = ("apple", "banana", "cherry")
print(my_tuple * 2)  # ("apple", "banana", "cherry", "apple", ...