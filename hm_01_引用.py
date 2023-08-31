a = 1  # 本质：将数据1的地址保存到变量a中，通常理解：将1保存到a
b = a  # 本质：将变量a中的引用保存到变量b中，通常理解：将a的值给b
print(a, b)
print(f'a:{a},{id(a)}')
print(f'a:{b},{id(b)}')
a = 2  # 本质：将数据2的地址保存到变量a中，只是改变a的引用，即改变a的值，没有改变b的引用
print(f'a:{a},{id(a)}')
print(f'a:{b},{id(b)}')

my_list = [1, 2, 3]
my_list1 = my_list
print(f'my_list:{my_list},{id(my_list)}')
print(f'my_list1:{my_list1},{id(my_list1)}')
my_list[1] = 10  # 修改列表中下标为1位置的引用
print(f'my_list:{my_list},{id(my_list)}')
print(f'my_list1:{my_list1},{id(my_list1)}')
