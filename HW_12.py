import requests
import csv
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список не повторяющихся цитат. Если автор не указан, цитату не брать.

url = "http://api.forismatic.com/api/1.0/"

def get_data_quotes(number):
    list_quote = []
    for numb in range(number):
        params = {"method": "getQuote",
                  "format": "json",
                  "key": numb,
                  "lang": "en"}
        r = requests.get(url, params=params)
        data = r.json()
        if data["quoteAuthor"] == "" or data in list_quote:
            continue
        else:
            list_quote.append([data["quoteAuthor"], data["quoteText"], data["quoteLink"]])
    return list_quote


# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# Имя файла сделать параметром по умолчанию.
# Заголовки csv файла:
# Author, Quote, URL.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
# Разделитель - запятая.

def write_quote_csv(number, filename="quotes.csv"):
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile)
        header = ["Author", "Quote", "URL"]
        quote_data = get_data_quotes(number)
        sorted_list = sorted(quote_data, key=lambda x: x[0])
        data = [header] + sorted_list
        writer.writerows(data)


write_quote_csv(5)
