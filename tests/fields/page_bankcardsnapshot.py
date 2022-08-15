#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-15 22:07:37
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-15 22:07:38
* @FilePath    : /guanfu/tests/fields/page_bankcardsnapshot.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import justpy
from guanfu.fieldtype.bankcard import FieldBankCardSnapshot



async def comp_test():
    wp = justpy.WebPage()
    FieldBankCardSnapshot(a=wp)
    return wp

justpy.justpy(comp_test)