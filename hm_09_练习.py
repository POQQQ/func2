"""定义一个函数，my_sum，作用，可以对任意多个数字进行求和"""


def my_sum(*args):  # *args是元组
    num = 0
    for i in args:
        num += i
    return num


# print(my_sum())
# print(my_sum(1, 2))
# print(my_sum(1, 2, 3, 4))
# print(my_sum(1, 5, 6, 9, 10))

my_list = [1, 2, 3, 4, 5]
# 需求 对列表中的所有数据使用my_sum函数进行求和
# 想要把列表（元组）中的数据作为位置参数进行传递，只需要在列表（元组）前边加上一个*，进行拆包即可
print(my_sum(*my_list))  # 15
