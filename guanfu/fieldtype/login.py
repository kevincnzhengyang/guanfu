#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-10 16:16:49
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-11 10:11:18
* @FilePath    : /guanfu/guanfu/fieldtype/login.py
* @Description : login with username and password
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''

import justpy


class FieldLogin(justpy.Div):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # layout
        self.classes = kwargs.get(
            "layout_class",
            "w-full md:w-full lg:w-9/12 mx-auto md:mx-0")

        # container
        c = justpy.Div(a=self,
                       classes=kwargs.get(
                            "container_class",
                            "bg-white p-10 flex flex-col w-full shadow-xl rounded-xl"))

        # title
        t = justpy.H2(a=c,
                      classes=kwargs.get(
                            "title_class",
                            "text-2xl font-bold text-gray-800 text-left mb-5"),
                      text=kwargs.get(
                            "title_text",
                            "Login"))

        # form
        f = justpy.Form(a=c, classes="w-full")
        # name group
        ng = justpy.Div(a=f,
                        classes=kwargs.get(
                            "group_class",
                            "flex flex-col w-full my-5"))
        ln = justpy.Label(a=ng,
                          classes=kwargs.get(
                                "label_class",
                                "text-gray-500 mb-2"),
                          text=kwargs.get(
                                "name_lable",
                                "Username"))
        inn = justpy.Input(a=ng,
                           classes=kwargs.get(
                                "input_class",
                                "appearance-none border-2 border-gray-100 rounded-lg px-4 py-3 placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-green-600 focus:shadow-lg"),
                           placeholder=kwargs.get(
                                "name_holder",
                                "Please insert your username"))
        # passwd group
        pg = justpy.Div(a=f,
                        classes=kwargs.get(
                            "group_class",
                            "flex flex-col w-full my-5"))
        lp = justpy.Label(a=ng,
                          classes=kwargs.get(
                                "label_class",
                                "text-gray-500 mb-2"),
                          text=kwargs.get(
                                "name_lable",
                                "Password"))
        inp = justpy.Input(a=ng,
                           type="password",
                           classes=kwargs.get(
                                "input_class",
                                "appearance-none border-2 border-gray-100 rounded-lg px-4 py-3 placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-green-600 focus:shadow-lg"),
                           placeholder=kwargs.get(
                                "password_holder",
                                "Please insert your password"))
        # button group
        bg = justpy.Div(a=f,
                        classes=kwargs.get(
                            "group_class",
                            "flex flex-col w-full my-5"))
        btn = justpy.Button(a=bg,
                            classes=kwargs.get(
                                "button_class",
                                "w-full py-4 bg-green-600 rounded-lg text-green-100"))
        bd = justpy.Div(a=btn,
                        classes="flex flex-row items-center justify-center")
        sd = justpy.Div(a=bd,
                        classes="mr-2")
        svg = justpy.Svg(a=sd,
                         classes="w-6 h-6",
                         viewBox="0 0 24 24",
                         xmlns="http://www.w3.org/2000/svg",
                         fill="none",
                         stroke="currentColor")
        icon = justpy.Path(a=svg,
                           stroke_linecap="round",
                           stroke_linejoin="round",
                           stroke_width="2",
                           d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1")
        bt = justpy.Div(a=bd,
                        classes=kwargs.get(
                            "button_text_class",
                            "font-bold"),
                        text=kwargs.get(
                            "button_text",
                            "Login"))

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

        if kwargs.get("with_link", False):
            # link group
            lg = justpy.Div(a=bg,
                            classes=kwargs.get(
                                "link_class",
                                "flex justify-evenly mt-5"))
            justpy.A(a=lg,
                    classes=kwargs.get(
                                "link_class",
                                "w-full text-center font-medium text-gray-500"),
                    text=kwargs.get(
                                "link1_text",
                                "Recover password!"),
                    href=kwargs.get(
                                "link1_href",
                                "#"))
            justpy.A(a=lg,
                    classes=kwargs.get(
                                "link_class",
                                "w-full text-center font-medium text-gray-500"),
                    text=kwargs.get(
                                "link2_text",
                                "Singup!"),
                    href=kwargs.get(
                                "link2_href",
                                "#"))
