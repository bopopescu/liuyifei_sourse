# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
# Python 2.x使用这行
#from Tkinter import *
# Python 3.x使用这行
from tkinter import *  
class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()
    def initWidgets(self):
        # 创建第一个容器
        fm1 = Frame(self.main)
        # 该容器放在左边排列
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 向fm1中添加3个按钮
        # 设置按钮从顶部开始排列，且按钮只能在垂直（X）方向填充
        Button(fm1, text='第一个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第二个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第三个').pack(side=TOP,  fill=X, expand=YES)
        # 创建第二个容器
        fm2 = Frame(self.main)
        # 该容器放在左边排列，就会挨着fm1
#        fm2.pack(side=LEFT, padx=10, expand=YES)
        fm2.pack(side=LEFT, padx=10, fill=BOTH, expand=YES)
        # 向fm2中添加3个按钮
        # 设置按钮从右边开始排列
        Button(fm2, text='第一个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第二个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第三个').pack(side=RIGHT, fill=Y, expand=YES)        
        # 创建第三个容器
        fm3 = Frame(self.main)
        # 该容器放在右边排列，就会挨着fm1
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        # 向fm3中添加3个按钮
        # 设置按钮从底部开始排列，且按钮只能在垂直（Y）方向填充
        Button(fm3, text='第一个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y, expand=YES) 
root = Tk()
root.title("Pack布局")
display = App(root)
root.mainloop()