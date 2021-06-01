class GetDataFromFiles:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.get_data()
        self.list_date = self.get_list_date()

    def get_data(self):
        with open(self.filename, "r") as txt_file:
            data = txt_file.readlines()
        return data

    def get_domains(self):
        return [items.replace(".", "").replace("\n", "") for items in self.data]

    def get_lastnames(self):
        return [items.split("\t")[1] for items in self.data]

    def get_list_date(self):
        return [line.split(" -")[0] for line in self.data if line[0].isdigit() and line.split(" -")[0][-1].isdigit()]

    def get_day(self):
        list_day = [date.split(" ")[0].rstrip("nsthrd") for date in self.list_date]
        day_modified_list = []
        for day in list_day:
            if len(day) == 1:
                day_modified_list.append("0" + day)
            else:
                day_modified_list.append(day)
        return day_modified_list

    def get_months(self):
        months_dict = {"January": "01",
                       "February": "02",
                       "March": "03",
                       "April": "04",
                       "May": "05",
                       "June": "06",
                       "July": "07",
                       "August": "08",
                       "September": "09",
                       "October": "10",
                       "November": "11",
                       "December": "12"}
        list_months = [date.split(" ")[1] for date in self.list_date]
        months_modified_list = [months_dict[months] for months in list_months]
        return months_modified_list

    def get_years(self):
        return [date.split(" ")[2] for date in self.list_date]

    def create_list_date_dict(self):
        date_original = [{"date_original": date} for date in self.list_date]
        date_modified = ["/".join(data) for data in list(zip(self.get_day(), self.get_months(), self.get_years()))]
        for index, date in enumerate(date_original):
            date["date_modified"] = date_modified[index]
        return date_original

#1
print(GetDataFromFiles("domains.txt").get_domains())
#2
print(GetDataFromFiles("names.txt").get_lastnames())
#3
print(GetDataFromFiles("authors.txt").create_list_date_dict())

