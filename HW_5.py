# my_number = 565844005460260000
# my_symbol = "0"
# count = (str(my_number)).count(my_symbol)
# print(count)

##################################################

# my_number = 56584400546026000
# count = len(str(my_number))-len(str(int(str(my_number)[::-1])))
# print(count)

##################################################

# my_list_1 = ["q", "a", "2", "7"]
# my_list_2 = ["y", "r", "u", "20"]
# my_result = []
# for symbol_1 in my_list_1[::2]:
#     my_result.append(symbol_1)
# for symbol_2 in my_list_2[1::2]:
#     my_result.append(symbol_2)
# print(my_result)

##################################################

# my_list = [1,2,3,4]
# new_list = []
# new_list.extend(my_list[1:])
# new_list.append(my_list[0])
# print(new_list)

##################################################

# my_list = [1,2,3,4]
# my_list.append(my_list[0])
# my_list.pop(0)
# print(my_list)

##################################################

# my_str = "43 больше чем 34 но меньше чем 56"
# res = [int(value) for value in my_str.split() if value.isdigit()]
# print(sum(res))

##################################################

# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
# start = my_str.find(l_limit)
# end = my_str.rfind(r_limit)
# sub_str = my_str[start + 1 : end]
# print(sub_str)

##################################################

my_str = "1234567"
my_list = []
