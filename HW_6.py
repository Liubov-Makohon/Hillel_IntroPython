# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

my_list = ["123", "qwe", "asd", "789"]
new_list = [my_list[index] if not index % 2 else my_list[index][::-1] for index in range(len(my_list))]
print(new_list)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ["123", "qwe", "asd", "789", "uau", "Add", "amm"]
new_list = [my_list[index] for index in range(len(my_list)) if my_list[index].startswith("a")]
print(new_list)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ["123", "qwe", "asd", "789", "uau", "Add", "amm"]
new_list = [my_list[index] for index in range(len(my_list)) if "a" in my_list[index]]
print(new_list)

# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = [123, "qwe", "asd", 789, "uau", "Add", "amm"]
new_list = [my_list[index] for index in range(len(my_list)) if type(my_list[index]) is str]
print(new_list)

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = "qwerty111222"
my_list = []
for symbol in set(list(my_str)):
    count = list(my_str).count(symbol)
    if count == 1:
        my_list.append(symbol)
print(my_list)

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "qwerty111test222"
my_str_2 = "qwerty111books222"
my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)
my_list = list(my_set_1.intersection(my_set_2))
print(my_list)

#
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str_1 = "qwerty111test2223"
my_str_2 = "qwerty111books2223"
my_set_1 = set([symbol for index, symbol in enumerate(list(my_str_1)) if list(my_str_1).count(symbol) < 2])
my_set_2 = set([symbol for index, symbol in enumerate(list(my_str_2)) if list(my_str_2).count(symbol) < 2])
my_list = list(my_set_1.intersection(my_set_2))
print(my_list)

# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

person = {"Фамилия": "Иванов",
          "Имя": "Георгий",
          "Возраст": "26",
          "Проживание": {"Страна": "Украина",
                         "Город": "Днепр",
                         "Улица": "Старокозацкая"},
          "Работа": {"Наличие": "Трудоустроен",
                     "Должность": "Юрисконсульт"}}

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло

recipe = {"Составляющие":
              {"Коржи":
                   {"Мука": "500 гр",
                    "Молоко": "200 мл",
                    "Масло": "50 гр",
                    "Яйцо": "2 шт"},
               "Крем":
                   {"Сахар": "200 гр",
                    "Масло": "100 гр",
                    "Ваниль": "2 гр",
                    "Сметана": "400 гр"},
               "Глазурь":
                   {"Какао": "75 гр",
                    "Сахар": "75 гр",
                    "Масло": "60 гр"}}}

