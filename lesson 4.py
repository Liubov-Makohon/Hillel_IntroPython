# # p = print("111")
# # print(p)
#
# # str = "d'artanian"
#
# # print(str.rfind('n'))
#
# # value = input()
# # if value.isdigit():
# #     res = int(value)
# #     print(res * 3)
#
# # my_t = (1, 2, 3, 3.14, 'qwe', 'tuple')
# # my_l = [1, 2, 3, 3.14, 'qwe', 'list']
#
# # print(my_t, type(my_t))
# # print(my_l, type(my_l))
# #
# # new_t = tuple(my_l)
# # new_l = list(my_t)
# #
# # print(new_t, type(new_t))
# # print(new_l, type(new_l))
# #
# # print(my_t[0], my_l[-1])
# #
# # index = 4
# # value_t = my_t[index]
# # print(value_t)
# # print(my_l)
# # my_l[0] = 'test'
# # print(my_l)
#
# # my_list_tuple = ([1,2], my_l)
# # my_list_tuple[0][1] = 'test'
# # print(my_list_tuple)
#
# # new_list = [[1], [2]] * 3
# # print(new_list)
#
# # test_list = [1,2,3]
# # print(id(test_list))
# #
# # new_list = [test_list.copy()] * 3
# # print(new_list, id(new_list[-1]))
# #
# # test_list[-1] = 'test'
# # print(test_list)
# # print(new_list)
#
#
# # my_list = []
# # my_list.append('a')
# # my_list.append('v')
# # my_list.pop()
# # print(my_list)
#
# # test_list = list('qwerty')
# # test_list[1] = 'W'
# # print(test_list)
# # new_str = ''.join(test_list)
# # print(new_str)
#
#
# my_list = ['q', 'a', '3', 'fox', '123']
#
# for value in my_list:
#     if not value.isdigit():
#         print(value)

# str = '0123456789'
#
# for value_1 in str:
#     for value_2 in str:
#         str.append(value_1 + value_2)
#         print(new_str)

l = ['a', 'b', 'c', 'd', 'e', 'f']
s = "_".join(l[::2])




print(s)