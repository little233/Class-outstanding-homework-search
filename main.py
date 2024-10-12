import os
import re
def visitDir(path):
    """
    遍历指定目录下的所有文件，并提取其中的中文字符。

    参数:
    path(str): 要遍历的目录路径。

    返回:
    无直接返回值，但会打印出错误信息（如果目录不存在或不是文件夹）。
    """
    # 初始化列表，用于后续存储文件名中的中文字符
    ls=list()
    
    # 检查给定路径是否为有效文件夹
    if not os.path.isdir(path):
        #判断文件夹是否为空
        print('Error: "', path, '" is not a directory or does not exist.')
        return
    else:
        # 定义全局变量x和s，x用于计数，s用于存储中文字符
        global x
        global s
        
        try:
            # 捕获异常，以处理可能发生的错误
            for lists in os.listdir(path):
                # 通过os遍历文件名到lists
                x += 1
                # 使用正则表达式提取文件名中的中文字符，并将其连接成一个字符串
                res = ''.join(re.findall('[\u4e00-\u9fa5]',lists))
                s+=res
                s+=" "
        except:
            # 如果发生异常，忽略并继续执行
            pass

def str_split(s, sp):
    """
    将字符串s按照分隔符sp进行分割，并返回分割后的字符串。
    
    参数:
    s: 待分割的原始字符串。
    sp: 用于分割字符串的分隔符。
    
    返回:
    分割后的字符串。
    """
    # 将s转换为字符串类型以确保输入的s总是字符串
    temp = str(s)
    # 初始化一个空字符串，用于存储分割后的字符
    ch = ""
    # 使用分隔符sp对字符串进行分割，得到一个字符串列表
    temp = temp.split(sp)
    # 遍历分割后的字符串列表，将每个元素逐个添加到ch中
    for c in temp:
        ch += c
    # 返回拼接后的字符串
    return ch

def diff(s, list_name):
    """
    输出两个列表的差集，即未上交作业的人员名单。

    本函数首先将两个列表转换为集合，然后通过集合的差集操作，
    找出在s中但不在list_name中的元素（这些元素将是在s中但未在list_name中上报的作业人员），
    以及在list_name中但不在s中的元素（这些元素将是已上报但不在s中的作业人员）。
    最后，将这两个差集合并成一个列表，并输出结果。

    :param s: 第一个列表，可以是班级所有人员名单或已上交作业的人员名单。
    :param list_name: 第二个列表，与s对应，可以是班级所有人员名单或已上交作业的人员名单。
    :return: 无返回值，直接打印出未上交作业的人员名单和一个布尔值。
             如果所有人都已上交作业，输出True，否则输出False。
    """
    # 进行差集运算，找出未上交作业的人员
    diff = list(set(s).difference(set(list_name)))
    diff.extend(list(set(list_name).difference(set(s))))

    # 打印未上交作业的人员名单
    print("未上交作业人员：", diff)
    # 如果差集为空，即所有人都已上交作业，输出True；否则，输出False
    if diff == []:
        print(True)
    else:
        print(False)

def text():
    """
    读取txt文件内容。
    
    该函数用于打开一个指定路径的文本文件，读取其内容，并在操作完成后关闭文件。
    使用'utf-8'编码以确保正确读取中文字符。
    
    Returns:
        str: 文件中的内容。
    """
    path="D:\PYTHONpj\work_cass_name\jk5.txt"# 对比姓名的文件位置#
    # 打开文件，使用'utf-8'编码读写
    fo = open(path, "r+", encoding='utf-8')
    # 读取文件内容
    str = fo.read()
    # 关闭文件
    fo.close()
    return str

def s_c(submitted):
    """
    处理班级作业提交情况。

    该函数读取一个文本文件中的班级成员名单，并与已上交作业的人员列表进行对比。
    它输出班级成员和已上交作业人员的信息，并计算出未上交作业的人员名单。

    参数:
    submitted (list or str): 已上交作业的人员列表或字符串。

    返回:
    None
    """
    # 根据输入类型处理已提交的作业信息
    if isinstance(submitted, str):
        submitted = submitted.split()  # 假设字符串中各个名字之间用空格分隔

    # 从文本文件中读取班级成员名单
    list_name = text().split("\n")  # 将文本按行分割成列表
    print("班级成员：", list_name)  # 输出班级成员名单
    print("已上交作业人员:", submitted)  # 输出已上交作业的人员名单
    diff(submitted, list_name)  # 调用差集函数，计算未上交作业的人员名单

def list_to_str():
    """
    获取已上交作业的人员名单和班级成员名单，并以列表形式输出。
    
    此函数首先获取已上交作业的人员名单，然后获取班级成员名单，
    通过用户输入的方式，使用'end'作为结束输入的标志。
    """
    # 获取已上交作业的人员名单
    # 初始化一个空列表来存储名字
    names_list = []

    # 设置结束标志
    end_marker = "end"

    # 循环读取用户输入，直到遇到结束标志
    print("请输入姓名，输入“end”结束输入")
    while True:
        # 提示用户输入名字
        name = input()

        # 判断是否为结束标志
        if name == end_marker:
            break  # 结束循环

        # 将输入的名字添加到列表中
        names_list.append(name)

    # 打印最终的名字列表
    print("已上交作业的人员名单:", names_list)

    # 获取班级成员名单
    # 初始化一个空列表来存储班级成员名字
    class_list = []
    print("请输入班级成员名单（以end结束）: ")
    while True:
        # 提示用户输入名字
        name = input()

        # 判断是否为结束标志
        if name == end_marker:
            break  # 结束循环

        # 将输入的名字添加到列表中
        class_list.append(name)
    # 打印班级成员名单
    print(class_list)
    # 处理并输出结果
    diff(names_list, class_list)


if __name__ == '__main__':
    # 初始化计数器x为0，用于统计权限文件数量
    x = 0
    # 初始化字符串s为空，用于后续处理
    s = ""

    # 用户选择输入方式
    choice = input("请选择输入方式：1. 输入目录路径 2. 直接输入名单\n")

    if choice == '1':
        # 用户输入一个目录路径
        b = input("请输入path: ")
        # 调用visitDir函数，传入用户输入的路径，开始访问目录
        visitDir(b)
        # 打印统计结果：权限文件的总数
        print('Total Permission Files: ', x)
        # 对字符串s进行分割处理，使用不同的分隔符
        s = str_split(s, sp="数据")
        s = str_split(s, sp="班")
        s = str_split(s, sp="和")
        s = str_split(s, sp="作业")
        # 对处理后的字符串s进行进一步的分割和处理
        s_c(s.split(" "))
    elif choice == '2':
        list_to_str()

    else:
        print("无效的选择，请输入 1 或 2。")

# if __name__ == '__main__':
#
#     # 初始化计数器x为0，用于统计权限文件数量
#     x = 0
#     # 初始化字符串s为空，用于后续处理
#     s=""
#     # 用户输入一个目录路径
#     b=input("请输入path")
#     # 调用visitDir函数，传入用户输入的路径，开始访问目录
#     visitDir(b)
#     # 打印统计结果：权限文件的总数
#     print('Total Permission Files: ', x)
#     # 对字符串s进行分割处理，使用不同的分隔符
#     s=str_split(s,sp="数据")
#     s=str_split(s,sp="班")
#     s=str_split(s,sp="和")
#     s=str_split(s,sp="作业")
#     # 对处理后的字符串s进行进一步的分割和处理
#     s_c(s.split(" "))


#本程序资料参考
# os读取文件夹文件路径：https://blog.csdn.net/xyisv/article/details/78035986
# 提取汉字：https://blog.csdn.net/qq_27900321/article/details/126837662
# 通过set()进行列表对比：https://www.runoob.com/python/python-func-set.html
#                    https://www.csdn.net/tags/MtTaAgwsOTQ0MzUtYmxvZwO0O0OO0O0O.html
