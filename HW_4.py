my_list = [8, 35, 5, 120, 56, 113, 100, 802]
for value in my_list:
    if value > 100:
        print(value)

#################################################

my_list = [8, 35, 5, 120, 56, 113, 100, 802]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)

#################################################

my_list = [8, 35, 5, 120, 56, 113, 100, 802]
if len(my_list) < 2:
    my_list.append(0)
elif len(my_list) >= 2:
    my_list.append(my_list[-1]+my_list[-2])
print(my_list)

#################################################

my_string = "0123456789"
my_result = []
for value_1 in my_string:
    for value_2 in my_string:
        my_result.append(value_1 + value_2)
print(my_result)

