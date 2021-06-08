# import os
# path=input('请输入文件路径(结尾加上/)：')
#
# #获取该目录下所有文件，存入列表中
# fileList=os.listdir(path)
# n=0
# for i in fileList:
#
#     #设置旧文件名（就是路径+文件名）
#     oldname=path+ os.sep + fileList[n]   # os.sep添加系统分隔符
#
#     #设置新文件名
#     newname=path + os.sep +'000'+str(n+877)+'.png'
#
#     os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
#     print(oldname,'======>',newname)
#
#     n+=1
#coding=utf-8


#批量修改文件名按照顺序排列
# wirtten by xh, 2018-4-1
#导入模块
import os
#获取输入路径
path=input('请输入文件路径(结尾加上/)：')
#获取该目录下所有文件，存入列表中
f=os.listdir(path)
#对获取的文件名进行排序,否则是乱序修改
f.sort()
n=0
s=str(n+877) #将int转换为string，从1开始
s = s.zfill(6) #字符串长度设置，不足左补零
#遍历修改每一个文件名
for i in f:
    #获取旧文件名（就是路径+文件名）
    oldname=path+f[n]
    #设置新文件名，根据自己的文件名和类型修改
    newname=path+s+'.png'
    #newname = path + os.sep +  str(n + 877) + '.png'
    #调用rename()重命名函数
    os.rename(oldname,newname)
    #打印修改结果
    print(oldname,'------------>',newname)
    #更新字符串
    n += 1
    s = str(n+944)
    s = s.zfill(6)
