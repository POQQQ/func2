my_tuple = (1, 2, [10, 20])  # 元组中存储的1的地址，2的地址，列表的地址

print(my_tuple, id(my_tuple), id(my_tuple[-1]), id(my_tuple[-1][-1]))
my_tuple[-1][-1] = 90  # 修改的列表中最后一个位置的引用
print(my_tuple, id(my_tuple), id(my_tuple[-1]), id(my_tuple[-1][-1]))
