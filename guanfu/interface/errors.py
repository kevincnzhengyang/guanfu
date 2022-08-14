#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-14 20:17:28
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-14 20:22:23
* @FilePath    : /guanfu/guanfu/interface/errors.py
* @Description : errors in integration api
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''

class APINetworkError(RuntimeError):
    pass


class APIAccountError(RuntimeError):
    pass


class APIPasswordError(RuntimeError):
    pass


class APISystemError(RuntimeError):
    pass
