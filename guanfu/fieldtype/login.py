#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-10 16:16:49
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-15 22:20:46
* @FilePath    : /guanfu/guanfu/fieldtype/login.py
* @Description : login with username and password
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''

from email import message
from socket import timeout
import justpy
import logging

from guanfu.utils.funcs import args_default, ui_notify, ui_input_error
from guanfu.interface.user import UserIn
from guanfu.interface.im_api import login_api
import guanfu.interface.errors as ae


class FieldLogin(justpy.Div):
    _layout_class = "q-pa-md"
    _container_class = "q-gutter-md"
    _title_class = "text-2xl font-bold text-gray-800 text-left mb-5"
    _group_class = "w-full my-5"
    _label_class = "text-gray-500 mb-2"
    _input_class = "appearance-none border-2 border-gray-100 rounded-lg px-4 py-3 placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-green-600 focus:shadow-lg"
    # _button_class = "w-full py-4 bg-green-600 rounded-lg text-green-100"
    # _button_text_class = "font-bold"
    _link_group_class = "flex justify-evenly mt-5"
    # _link_class = "w-full text-center font-medium text-gray-500"

    def __init__(self, **kwargs):
        """
        widgets:
        - container
        - title
        - account
        - password
        - submit
        - links
        """
        # handle parameters
        params = {w: kwargs.pop(f"_{w}", dict()) for w in [
            "container", "title", "account", "password",
            "submit", "links"]}
        self.login_status = False
        self.user_data = None

        # using kwargs for root layout
        args_default(kwargs, {"classes": FieldLogin._layout_class})
        super().__init__(**kwargs)

        # container
        args_default(params["container"],
                {"a": self,
                 "classes": FieldLogin._container_class,
                 "style": "max-width: 300px"})
        c = justpy.Div(**params["container"])

        # title
        args_default(params["title"],
                {"a": c,
                 "classes": FieldLogin._title_class,
                 "text": "Login"})
        justpy.H3(**params["title"])

        # form
        f = justpy.Form(a=c, classes="w-full")
        # account
        args_default(params["account"],
                {"a": f,
                 "name": "account",
                 "error": False,
                 "autofocus": True,
                 "label": "User name",
                 "hint": "using account in IM linke MatterMost",
                 "hide-hint": True,
                 "clearable": True,
                 "clear-icon": "close",
                 "outlined": True,
                 "input-class": FieldLogin._input_class,
                 "rounded": True})
        self.ipt_account = justpy.QInput(**params["account"])
        self.ipt_account.on("input", self.input_ready)

        # passwd
        args_default(params["password"],
                {"a": f,
                 "type": "password",
                 "name": "password",
                 "error": False,
                 "autofocus": False,
                 "label": "Password",
                 "hint": "using password in IM linke MatterMost",
                 "hide-hint": True,
                 "outlined": True,
                 "input-class": FieldLogin._input_class,
                 "rounded": True})
        self.ipt_password = justpy.QInput(**params["password"])
        self.ipt_password.on("input", self.input_ready)

        visibility_icon = justpy.QIcon(name='visibility_off', classes='cursor-pointer')
        visibility_icon.password_input = self.ipt_password

        self.ipt_password.append_slot = visibility_icon

        def toggle_password(self, msg):
            if self.name == 'visibility_off':
                self.name = 'visibility'
                self.password_input.type='text'
            else:
                self.name = 'visibility_off'
                self.password_input.type = 'password'

        visibility_icon.on('click', toggle_password)

        # button
        bg = justpy.Div(a=f, classes=FieldLogin._group_class)

        args_default(params["submit"],
                {"a": bg,
                 "type": "button",
                 "text": "Login",
                 "size": "lg",
                 "disable": True,
                 "rounded": True,
                 "color": "primary",
                 "icon": "navigation",
                 "push": True})
        self.btn_submit = justpy.QButton(**params["submit"])
        self.btn_submit.on("click", self.invoke_login)


        # btn = justpy.Button(a=bg,
        #                     classes=kwargs.get(
        #                         "button_class",
        #                         FieldLogin._button_class))
        # bd = justpy.Div(a=btn,
        #                 classes="flex flex-row items-center justify-center")
        # sd = justpy.Div(a=bd,
        #                 classes="mr-2")
        # svg = justpy.Svg(a=sd,
        #                  classes="w-6 h-6",
        #                  viewBox="0 0 24 24",
        #                  xmlns="http://www.w3.org/2000/svg",
        #                  fill="none",
        #                  stroke="currentColor")
        # justpy.Path(a=svg,
        #             stroke_linecap="round",
        #             stroke_linejoin="round",
        #             stroke_width="2",
        #             d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1")
        # justpy.Div(a=bd,
        #             classes=kwargs.get(
        #                 "button_text_class",
        #                 FieldLogin._button_text_class),
        #             text=kwargs.get(
        #                 "button_text",
        #                 "Login"))

        if kwargs.get("with_google", False):
            # with Google Account
            # TODO
            pass
        if kwargs.get("with_github", False):
            # with Github Account
            # TODO
            pass
        if kwargs.get("with_twitter", False):
            # with Twitter Account
            # TODO
            pass

        # link group
        lg = justpy.Div(a=f, classes=FieldLogin._link_group_class)
        args_default(params["links"],
                {"a": lg,
                 "type": "a",
                 "rounded": True,
                 "color": "primary",
                 "flat": True,
                 "l0_lable": "Recover password!",
                 "l0_href": "#",
                 "l1_lable": "Singup!",
                 "l1_href": "#"})
        justpy.QButton(text=params["links"]["l0_lable"],
                       align="left",
                       href=params["links"]["l0_href"],
                       **params["links"])
        justpy.QButton(text=params["links"]["l1_lable"],
                       align="right",
                       href=params["links"]["l1_href"],
                       **params["links"])

        self.notification = justpy.QNotify(a=self, position="bottom", closeBtn='Close', timeout=3000)

    def input_ready(self, msg):
        self.login_status = False
        if self.ipt_account.value.strip() and self.ipt_password.value.strip():
            self.btn_submit.disable = False
        else:
            self.btn_submit.disable = True

    def invoke_login(self, msg):
        try:
            self.user_data = login_api(user=UserIn(
                                            account=self.ipt_account.value,
                                            password=self.ipt_password.value))
            self.login_status = True
        except ValueError as e:
            # validation error happened in UserIn
            logging.info(f"login, UserIn model failed {self.ipt_account.value}")
            ui_notify(self, message="Validate Failed", caption=f"{e}")
        except  ae.APIAccountError as e:
            ui_input_error(self.ipt_account, "Account Invalid")
        except ae.APIPasswordError as e:
            ui_input_error(self.ipt_password, "Password Invalid")
        except ae.APINetworkError as e:
            logging.error(f"login, network disconnect")
            ui_notify(self, message="Network Failed", caption=f"{e}")
        except ae.APISystemError as e:
            logging.error(f"login, IM system failed to response")
            ui_notify(self, message="System Failed", caption=f"{e}")
