#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-14 11:57:26
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-15 22:27:03
* @FilePath    : /guanfu/guanfu/utils/funcs.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from justpy import QInput


def args_default(args: dict, params: dict) -> None:
    if args is None:
        raise ValueError(f"set default value to None")

    # ignore existed
    # [params.pop(k) for k in params.keys() if k in args.keys()]
    args.update({k: params[k] for k in (set(params.keys()) - set(args.keys()))})


def ui_notify(obj, message: str, caption: str = None) -> None:
    if not hasattr(obj, "notification"):
        return
    obj.notification.notify = True
    obj.notification.message = message
    obj.notification.caption = caption


def ui_input_error(obj, message: str) -> None:
    if not isinstance(obj, QInput):
        raise ValueError(f"can't show QInput error with {type(obj)}")

    obj.error = True
    obj.error_message = message
