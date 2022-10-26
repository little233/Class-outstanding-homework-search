import os
import re
def visitDir(path):
    ls=list()
    if not os.path.isdir(path):
        #判断文件夹是否为空
        print('Error: "', path, '" is not a directory or does not exist.')
        return
    else:
        global x
        global s
        try:
            #捕获异常
            for lists in os.listdir(path):
                #通过os遍历文件名到lists
                #print(lists)
                x += 1
                res = ''.join(re.findall('[\u4e00-\u9fa5]',lists))
                s+=res
                s+=" "
        except:
            pass
def str_split(s,sp):
    #字符串通过sp进行分割返回字符串
    temp=str(s)
    ch=""
    temp=temp.split(sp)
    for c in temp:
        ch+=c
    return ch
def diff(s,list_name):
    #进行差集运算
    diff = list(set(s).difference(set(list_name)))
    diff.extend(list(set(list_name).difference(set(s))))

    print("未上交作业人员：",diff)
    if diff == []:
        print(True)
    else:
        print(False)
def text():   #读取txt文件
    path="D:\PYTHONpj\work_cass_name\classname.txt"# 对比姓名的文件位置#
    #读写打开，指定编码
    fo = open(path, "r+",encoding='utf-8')
    str = fo.read()
    # 关闭打开的文件
    fo.close()
    return str
def s_c(s):
    #对读取到的txt文本做格式处理并将传入的列表，一起传入差集函数中
    list_name=text()
    list_name=list_name.split("\n")
    print("班级成员：",list_name)
    print("已上交作业人员:",s)
    diff(s,list_name)
if __name__ == '__main__':
    x = 0
    s=""
    b=input("请输入path")
    visitDir(b)
    print('Total Permission Files: ', x)
    s=str_split(s,sp="数据")
    s=str_split(s,sp="班")
    s=str_split(s,sp="和")
    s_c(s.split(" "))




#本程序资料参考
# os读取文件夹文件路径：https://blog.csdn.net/xyisv/article/details/78035986
# 提取汉字：https://blog.csdn.net/qq_27900321/article/details/126837662
# 通过set()进行列表对比：https://www.runoob.com/python/python-func-set.html
#                    https://www.csdn.net/tags/MtTaAgwsOTQ0MzUtYmxvZwO0O0OO0O0O.html