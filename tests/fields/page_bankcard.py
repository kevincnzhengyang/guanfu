#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-12 23:39:01
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-13 15:55:20
* @FilePath    : /guanfu/tests/fields/page_bankcard.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from guanfu.fieldtype.bankcard import *



async def comp_test():
    wp = justpy.WebPage()
    ss = FieldBankCard(a=wp)
    return wp

justpy.justpy(comp_test)
