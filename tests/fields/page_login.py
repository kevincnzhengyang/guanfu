#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-12 23:38:29
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-15 11:08:16
* @FilePath    : /guanfu/tests/fields/page_login.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from guanfu.fieldtype.login import *



async def comp_test():
    wp = justpy.QuasarPage()
    ss = FieldLogin(a=wp)
    return wp

justpy.justpy(comp_test)