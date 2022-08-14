#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-14 14:49:22
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-14 20:32:34
* @FilePath    : /guanfu/guanfu/interface/user.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''

from pydantic import BaseModel, SecretStr, constr, NameEmail


class UserBase(BaseModel):
    account: constr(strip_whitespace=True, max_length=20)
    avatar: str = None
    full_name: str = None
    email: NameEmail = None
    token: str = None


class UserIn(UserBase):
    password: SecretStr
