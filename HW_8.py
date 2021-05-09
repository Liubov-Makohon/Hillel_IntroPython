import random as rnd
import string

#################################
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

def create_new_list(my_list):
    new_list = [my_list[index] if not index % 2 else my_list[index][::-1] for index in range(len(my_list))]
    return new_list


#################################
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

def create_start_a_list(my_list):
    new_list = [word for word in my_list if word.startswith("a")]
    return new_list


#################################
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

def create_with_a_list(my_list):
    new_list = [word for word in my_list if "a" in word]
    return new_list


#################################
# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

def create_string_list(my_list):
    new_list = [value for value in my_list if type(value) is str]
    return new_list


#################################
# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

def create_symbol_list(my_str):
    my_list = [symbol for symbol in my_str if my_str.count(symbol) == 1]
    return my_list


#################################
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

def create_cross_list(my_str_1, my_str_2):
    my_list = list(set(my_str_1).intersection(set(my_str_2)))
    return my_list


#################################
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

def create_unique_symbol_list(my_str_1, my_str_2):
    my_list = [symbol for symbol in my_str_1 if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1]
    return my_list


#################################
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

def generate_e_mail(names, domains):
    random_e_mail = f"{rnd.choice(names)}.{rnd.randint(100, 999)}@{''.join(rnd.choice(string.ascii_lowercase) for _ in range(rnd.randrange(5, 8)))}.{rnd.choice(domains)}"
    return random_e_mail


my_list = ["123", "qwe", "asd", "789", "uau", "Add", "amm"]
my_list_1 = [123, "qwe", "asd", 789, "uau", "Add", "amm"]
my_str = "qwerty111222"
my_str_1 = "qwerty111test222"
my_str_2 = "qwerty111books222"
names = ["moon", "nolan", "grey", "mitchell", "black"]
domains = ["net", "com", "ua", "org", "gov"]


task_1 = create_new_list(my_list)
task_2 = create_start_a_list(my_list)
task_3 = create_with_a_list(my_list)
task_4 = create_string_list(my_list_1)
task_5 = create_symbol_list(my_str)
task_6 = create_cross_list(my_str_1, my_str_2)
task_7 = create_unique_symbol_list(my_str_1, my_str_2)
task_8 = generate_e_mail(names, domains)
