import json
import re

# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

def json_reader(filename):
    with open(filename, "r", encoding='utf-8') as json_file:
      data = json.load(json_file)
    return data


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def sort_by_lastname(math_dict):
    return (math_dict["name"]).split(" ")[-1]


# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

def sort_by_death(math_dict):
    year = math_dict["years"]
    years = re.findall(r'[0-9BC]+', year)
    if "BC" in years[-1]:
        return -1 * int(years[-2])
    else:
        return int(years[-1])


# 4. Написать функцию сортировки по количеству слов в поле "text"

def sort_by_len_text(math_dict):
    text = math_dict["text"]
    len_text = len(re.findall(r'\w+', text))
    return len_text


filename = "data.json"

get_data = json_reader(filename)
print(get_data)

sort_lastname = sorted(json_reader(filename), key=sort_by_lastname)
print(sort_lastname)

sort_death_date = sorted(json_reader(filename), key=sort_by_death)
print(sort_death_date)

sort_len_text = sorted(json_reader(filename), key=sort_by_len_text)
print(sort_len_text)
