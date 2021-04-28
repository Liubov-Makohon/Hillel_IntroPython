# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.

persons = [{"name": "John", "age": 15}, {"name": "Adolf", "age": 56}, {"name": "Harry", "age": 26}, {"name": "Jack", "age": 45}]
age_list = [list(items.values())[1] for items in persons]
for items in persons:
    if list(items.values())[1] == min(age_list):
        print(list(items.values())[0])

# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.

persons = [{"name": "John", "age": 15}, {"name": "Adolf", "age": 56}, {"name": "Harry", "age": 26}, {"name": "Jack", "age": 45}]
name_list = [list(items.values())[0] for items in persons]
for name in name_list:
    if len(name) == len(max(name_list, key=len)):
        print(name)

# в) Посчитать среднее количество лет всех людей из списка.

persons = [{"name": "John", "age": 15}, {"name": "Adolf", "age": 56}, {"name": "Harry", "age": 26}, {"name": "Jack", "age": 45}]
age_list = [list(items.values())[1] for items in persons]
average = sum(age_list)//len(age_list)
print(average)


# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.

my_dict_1 = {1:11, 2:22, 3:33}
my_dict_2 = {10:1, 2:2, 3:3}
same_key_list = [key for key in my_dict_1 if key in my_dict_2]
print(same_key_list)


# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

my_dict_1 = {1:11, 2:22, 3:33}
my_dict_2 = {10:1, 2:2, 3:3}
key_list = [key for key in my_dict_1 if key not in my_dict_2]
print(key_list)


# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

my_dict_1 = {1:11, 2:22, 33:33}
my_dict_2 = {10:1, 2:2, 3:3}
new_dict = {key: value for key, value in my_dict_1.items() if key not in my_dict_2}
print(new_dict)


# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {1:11, 2:22, 33:33}
my_dict_2 = {10:1, 2:2, 3:3}
new_dict = {}

my_dicts = [my_dict_1, my_dict_2]
for dict in my_dicts:
    for key, value in dict.items():
        if new_dict.get(key) is None:
            new_dict[key] = value
        else:
            new_dict[key] = [dict[key] for dict in my_dicts if key in dict]
print(new_dict)
