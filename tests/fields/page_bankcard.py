#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-12 23:39:01
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-15 22:09:08
* @FilePath    : /guanfu/tests/fields/page_bankcard.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from guanfu.fieldtype.bankcard import *



async def comp_test():
    wp = justpy.QuasarPage()
    ss = FieldBankCard(a=wp)
    return wp

justpy.justpy(comp_test)
