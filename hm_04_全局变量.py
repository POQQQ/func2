# 定义全局变量
g_num = 10


def func_1():
    print(g_num)  # 使用全局变量


def func_2():
    g_num = 20
    print(g_num)


def func_3():
    global g_num  # 声明为全局变量
    g_num = 30
    print(g_num)


if __name__ == '__main__':
    print(g_num)
    func_1()
    func_2()
    func_1()
    print(g_num)
    func_3()
    func_1()
