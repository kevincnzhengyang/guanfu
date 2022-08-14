#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-14 11:57:26
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-14 12:06:26
* @FilePath    : /guanfu/guanfu/utils/funcs.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''


def args_default(args: dict, params: dict) -> None:
    if args is None:
        raise ValueError(f"set default value to None")

    # ignore existed
    [params.pop(k) for k in params.keys() if k in args.keys()]
    args.update(params)
