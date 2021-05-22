# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)


def get_data(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
    return data


# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).


def get_domains(filename):
    return [items.replace(".", "").replace("\n", "") for items in get_data(filename)]


# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"


def get_lastnames(filename):
    return [items.split("\t")[1] for items in get_data(filename)]


# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]


def get_list_date(filename):
    return [line.split(" -")[0] for line in get_data(filename) if line[0].isdigit() and line.split(" -")[0][-1].isdigit()]


def get_day(filename):
    list_day = [date.split(" ")[0].rstrip("nsthrd") for date in get_list_date(filename)]
    day_modified_list = []
    for day in list_day:
        if len(day) == 1:
            day_modified_list.append("0" + day)
        else:
            day_modified_list.append(day)
    return day_modified_list


def get_months(filename):
    list_months = [date.split(" ")[1] for date in get_list_date(filename)]
    months_modified_list = [months_dict[months] for months in list_months]
    return months_modified_list


def get_years(filename):
    return [date.split(" ")[2] for date in get_list_date(filename)]


def create_list_date_dict(filename):
    date_original = [{"date_original": date} for date in get_list_date(filename)]
    date_modified = ["/".join(data) for data in list(zip(get_day(filename), get_months(filename), get_years(filename)))]
    for index, date in enumerate(date_original):
        date["date_modified"] = date_modified[index]
    return date_original

months_dict = {"January": "01",
           "February": "02",
           "March": "03",
           "April":"04",
           "May": "05",
           "June": "06",
           "July": "07",
           "August": "08",
           "September": "09",
           "October": "10",
           "November": "11",
           "December": "12"}


list_domain = get_domains("domains.txt")
print(list_domain)

list_lastname = get_lastnames("names.txt")
print(list_lastname)

list_dict_date = create_list_date_dict("authors.txt")
print(list_dict_date)
