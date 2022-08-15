#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-12 16:11:03
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-15 22:30:52
* @FilePath    : /guanfu/guanfu/fieldtype/bankcard.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import justpy
import logging
from datetime import date, datetime
from pydantic import BaseModel
from pydantic.types import PaymentCardNumber, PaymentCardBrand, constr

from guanfu.utils.funcs import args_default, ui_notify, ui_input_error


class ModelCardNumber(BaseModel):
    holder: constr(strip_whitespace=True, min_length=1)
    number: PaymentCardNumber
    expires: date
    cvc: constr(strip_whitespace=True, regex="[0-9]{3}")

    class Config:
        validate_assignment = True


# TODO snapshot can't display in QuasarPage
class FieldBankCardSnapshot(justpy.Figure):
    _card_class = "w-max h-max relative select-none pointer-events-none"
    _verso_class = "z-1 absolute overflow-hidden transform translate-y-12 left-16 w-96 h-56 rounded-2xl bg-gray-100 shadow-2xl"
    _verso_bar_class = "w-full h-12 bg-gray-200 absolute top-10"
    _rect_class = "z-2 absolute overflow-hidden w-96 h-56 rounded-2xl px-8 py-6 bg-red-400 text-white shadow-xl flex flex-col justify-end gap-6"
    _logo_class = "absolute top-6 right-8 w-16 h-8 flex justify-items-center items-center"
    _chip_class = "w-11 h-7 rounded bg-yellow-100"
    _number_class = "whitespace-nowrap text-2xl font-semibold"
    _info_class = "flex gap-8"
    _info_group_class = "flex flex-col w-max"
    _info_lable_class = "text-xs uppercase"
    _info_text_class = "whitespace-nowrap text-lg"

    def __init__(self, **kwargs):
        """
        widgets:
        - card
        - verso
        - verso_bar
        - rect
        - logo
        - chip
        - number
        - info_label
        - info_text
        """
        # super().__init__(**kwargs)

        # # figure
        # self.classes = kwargs.get(
        #     "figure_class",
        #     "w-full") # "top-8 left-8")

        # # card div
        # cd = justpy.Div(a=self,
        #                 classes=kwargs.get(
        #                     "card_class",
        #                     FieldBankCardSnapshot._card_class))

        # # verso
        # verso = justpy.Div(a=cd,
        #                    classes=kwargs.get(
        #                         "verso_class",
        #                         FieldBankCardSnapshot._verso_class))
        # justpy.Div(a=verso,
        #            classes=kwargs.get(
        #                 "verso_bar_class",
        #                 FieldBankCardSnapshot._verso_bar_class),
        #            text=kwargs.get(
        #                 "verso_bar_text",
        #                 "&nbsp;"))

        # # recto
        # rd = justpy.Div(a=cd,
        #                 classes=kwargs.get(
        #                     "recto_class",
        #                     FieldBankCardSnapshot._rect_class))
        # #logo
        # ld = justpy.Div(a=rd,
        #                 classes=kwargs.get(
        #                     "logo_class",
        #                     FieldBankCardSnapshot._logo_class))
        # self.logo = justpy.Svg(a=ld, viewBox="0 0 1000 324.68")
        # # visa logo
        # self.show_brand(brand=kwargs.get("card_brand", PaymentCardBrand.visa))
        # if kwargs.get("with_chip", True):
        #     justpy.Div(a=rd,
        #                classes=kwargs.get(
        #                     "chip_class",
        #                     FieldBankCardSnapshot._chip_class),
        #                text="  ")
        # # number
        # self.number = justpy.Div(a=rd,
        #                          classes=kwargs.get(
        #                             "number_class",
        #                             FieldBankCardSnapshot._number_class),
        #                          style=kwargs.get(
        #                             "number_style",
        #                             "font-family:Courier new, mono;"),
        #                          text=kwargs.get(
        #                             "card_number",
        #                             "424242******4242"))
        # # info
        # # - holder
        # nd = justpy.Div(a=rd,
        #                 classes=kwargs.get(
        #                     "info_class",
        #                     FieldBankCardSnapshot._info_class))
        # hd = justpy.Div(a=nd,
        #                 classes=kwargs.get(
        #                     "info_group_class",
        #                     FieldBankCardSnapshot._info_group_class))
        # # -- label
        # justpy.Span(a=hd,
        #             classes=kwargs.get(
        #                 "info_label_class",
        #                 FieldBankCardSnapshot._info_lable_class),
        #             text=kwargs.get(
        #                 "holder_label",
        #                 "Card holder"))
        # # -- name
        # self.holder = justpy.Span(a=hd,
        #                         classes=kwargs.get(
        #                             "info_text_class",
        #                             FieldBankCardSnapshot._info_text_class),
        #                         text=kwargs.get(
        #                             "holder_text",
        #                             "John Doe"))
        # # - expires
        # ed = justpy.Div(a=nd,
        #                 classes=kwargs.get(
        #                     "info_group_class",
        #                     FieldBankCardSnapshot._info_group_class))
        # # -- label
        # justpy.Span(a=ed,
        #             classes=kwargs.get(
        #                 "info_label_class",
        #                 FieldBankCardSnapshot._info_lable_class),
        #             text=kwargs.get(
        #                 "expires_label",
        #                 "Expires"))
        # # -- date
        # self.expires = justpy.Span(a=ed,
        #                            classes=kwargs.get(
        #                                 "info_text_class",
        #                                 FieldBankCardSnapshot._info_text_class),
        #                            text=kwargs.get(
        #                                 "expires_text",
        #                                 "09/28"))
        # # - cvc
        # vd = justpy.Div(a=nd,
        #                 classes=kwargs.get(
        #                     "info_group_class",
        #                     FieldBankCardSnapshot._info_group_class))
        # # -- label
        # justpy.Span(a=vd,
        #             classes=kwargs.get(
        #                 "info_label_class",
        #                 FieldBankCardSnapshot._info_lable_class),
        #             text=kwargs.get(
        #                 "cvc_label",
        #                 "cvc"))
        # # -- cvc
        # self.cvc = justpy.Span(a=vd,
        #                        classes=kwargs.get(
        #                             "info_text_class",
        #                             FieldBankCardSnapshot._info_text_class),
        #                        text=kwargs.get(
        #                             "cvc_text",
        #                             "123"))

        # handle parameters
        params = {w: kwargs.pop(f"_{w}", dict()) for w in [
            "card", "verso", "verso_bar", "rect",
            "logo", "chip", "number", "info_label", "info_text"]}

        # using kwargs for figure
        args_default(kwargs, {"classes": "w-full"})
        super().__init__(**kwargs)

        # card div
        args_default(params["card"], {"a": self,
                            "classes": FieldBankCardSnapshot._card_class})
        cd = justpy.Div(**params["card"])

        # verso
        args_default(params["verso"], {"a": cd,
                            "classes": FieldBankCardSnapshot._verso_class})
        verso = justpy.Div(**params["verso"])
        args_default(params["verso_bar"], {"a": verso,
                            "classes": FieldBankCardSnapshot._verso_bar_class,
                            "text": "&nbsp;"})
        justpy.Div(**params["verso_bar"])

        # rect
        args_default(params["rect"], {"a": cd,
                            "classes": FieldBankCardSnapshot._rect_class})
        rd = justpy.Div(**params["rect"])

        #logo
        args_default(params["logo"], {"a": rd,
                            "classes": FieldBankCardSnapshot._logo_class})
        ld = justpy.Div(**params["logo"])

        self.logo = justpy.Svg(a=ld, viewBox="0 0 1000 324.68")
        # visa logo
        self.show_brand(brand=PaymentCardBrand.visa)
        args_default(params["chip"], {"a": rd,
                            "classes": FieldBankCardSnapshot._chip_class,
                            "text": "&nbsp;"})
        justpy.Div(**params["chip"])

        # number
        args_default(params["number"], {"a": rd,
                            "classes": FieldBankCardSnapshot._number_class,
                            "style": "font-family:Courier new, mono;",
                            "text": "424242******4242"})
        self.number = justpy.Div(**params["number"])

        # info
        # - holder
        nd = justpy.Div(a=rd, classes=FieldBankCardSnapshot._info_class)
        hd = justpy.Div(a=nd, classes=FieldBankCardSnapshot._info_group_class)
        # -- label
        args_default(params["info_label"], {"a": hd,
                            "classes": FieldBankCardSnapshot._info_lable_class,
                            "text": "Card holder"})
        justpy.Span(**params["info_label"])
        # -- name
        args_default(params["info_text"], {"a": hd,
                            "classes": FieldBankCardSnapshot._info_text_class,
                            "text": "John Doe"})
        self.holder = justpy.Span(**params["info_text"])
        # - expires
        ed = justpy.Div(a=nd, classes=FieldBankCardSnapshot._info_group_class)
        params["info_label"].update({"a": ed,
                    "text": "Expires"})
        justpy.Span(**params["info_label"])
        # -- date
        params["info_text"].update({"a": ed,
                    "text": "J09/28"})
        self.expires = justpy.Span(**params["info_text"])
        # - cvc
        vd = justpy.Div(a=nd, classes=FieldBankCardSnapshot._info_group_class)
        # -- label
        params["info_label"].update({"a": vd,
                    "text": "cvc"})
        justpy.Span(**params["info_label"])
        # -- cvc
        params["info_text"].update({"a": vd,
                    "text": "888"})
        self.cvc = justpy.Span(**params["info_text"])

    def show_brand(self, brand: str):
        self.logo.delete_components()
        if brand == PaymentCardBrand.visa:
            justpy.Path(a=self.logo,
                        fill="#fff",
                        d="m651.19 0.5c-70.933 0-134.32 36.766-134.32 104.69 0 77.9 112.42 83.281 112.42 122.42 0 16.478-18.884 31.229-51.137 31.229-45.773 0-79.984-20.611-79.984-20.611l-14.638 68.547s39.41 17.41 91.734 17.41c77.552 0 138.58-38.571 138.58-107.66 0-82.316-112.89-87.536-112.89-123.86 0-12.908 15.502-27.052 47.663-27.052 36.287 0 65.892 14.99 65.892 14.99l14.326-66.204s-32.213-13.897-77.642-13.897zm-648.97 4.9966-1.7176 9.9931s29.842 5.4615 56.719 16.356c34.607 12.493 37.072 19.765 42.9 42.354l63.511 244.83h85.137l131.16-313.53h-84.942l-84.278 213.17-34.39-180.7c-3.1539-20.681-19.129-32.478-38.684-32.478h-135.41zm411.87 0-66.634 313.53h80.999l66.4-313.53h-80.765zm451.76 0c-19.532 0-29.88 10.457-37.474 28.73l-118.67 284.8h84.942l16.434-47.467h103.48l9.9931 47.467h74.948l-65.385-313.53h-68.273zm11.047 84.707 25.178 117.65h-67.454l42.276-117.65z")
        elif brand == PaymentCardBrand.amex:
            # TODO update svg path data to amex
            justpy.Path(a=self.logo,
                        fill="#ff0",
                        d="m651.19 0.5c-70.933 0-134.32 36.766-134.32 104.69 0 77.9 112.42 83.281 112.42 122.42 0 16.478-18.884 31.229-51.137 31.229-45.773 0-79.984-20.611-79.984-20.611l-14.638 68.547s39.41 17.41 91.734 17.41c77.552 0 138.58-38.571 138.58-107.66 0-82.316-112.89-87.536-112.89-123.86 0-12.908 15.502-27.052 47.663-27.052 36.287 0 65.892 14.99 65.892 14.99l14.326-66.204s-32.213-13.897-77.642-13.897zm-648.97 4.9966-1.7176 9.9931s29.842 5.4615 56.719 16.356c34.607 12.493 37.072 19.765 42.9 42.354l63.511 244.83h85.137l131.16-313.53h-84.942l-84.278 213.17-34.39-180.7c-3.1539-20.681-19.129-32.478-38.684-32.478h-135.41zm411.87 0-66.634 313.53h80.999l66.4-313.53h-80.765zm451.76 0c-19.532 0-29.88 10.457-37.474 28.73l-118.67 284.8h84.942l16.434-47.467h103.48l9.9931 47.467h74.948l-65.385-313.53h-68.273zm11.047 84.707 25.178 117.65h-67.454l42.276-117.65z")
        elif brand == PaymentCardBrand.mastercard:
            # TODO update svg path data to mastercard
            justpy.Path(a=self.logo,
                        fill="#f0f",
                        d="m651.19 0.5c-70.933 0-134.32 36.766-134.32 104.69 0 77.9 112.42 83.281 112.42 122.42 0 16.478-18.884 31.229-51.137 31.229-45.773 0-79.984-20.611-79.984-20.611l-14.638 68.547s39.41 17.41 91.734 17.41c77.552 0 138.58-38.571 138.58-107.66 0-82.316-112.89-87.536-112.89-123.86 0-12.908 15.502-27.052 47.663-27.052 36.287 0 65.892 14.99 65.892 14.99l14.326-66.204s-32.213-13.897-77.642-13.897zm-648.97 4.9966-1.7176 9.9931s29.842 5.4615 56.719 16.356c34.607 12.493 37.072 19.765 42.9 42.354l63.511 244.83h85.137l131.16-313.53h-84.942l-84.278 213.17-34.39-180.7c-3.1539-20.681-19.129-32.478-38.684-32.478h-135.41zm411.87 0-66.634 313.53h80.999l66.4-313.53h-80.765zm451.76 0c-19.532 0-29.88 10.457-37.474 28.73l-118.67 284.8h84.942l16.434-47.467h103.48l9.9931 47.467h74.948l-65.385-313.53h-68.273zm11.047 84.707 25.178 117.65h-67.454l42.276-117.65z")
        else:
            # TODO update svg path data to others
            justpy.Path(a=self.logo,
                        fill="#0ff",
                        d="m651.19 0.5c-70.933 0-134.32 36.766-134.32 104.69 0 77.9 112.42 83.281 112.42 122.42 0 16.478-18.884 31.229-51.137 31.229-45.773 0-79.984-20.611-79.984-20.611l-14.638 68.547s39.41 17.41 91.734 17.41c77.552 0 138.58-38.571 138.58-107.66 0-82.316-112.89-87.536-112.89-123.86 0-12.908 15.502-27.052 47.663-27.052 36.287 0 65.892 14.99 65.892 14.99l14.326-66.204s-32.213-13.897-77.642-13.897zm-648.97 4.9966-1.7176 9.9931s29.842 5.4615 56.719 16.356c34.607 12.493 37.072 19.765 42.9 42.354l63.511 244.83h85.137l131.16-313.53h-84.942l-84.278 213.17-34.39-180.7c-3.1539-20.681-19.129-32.478-38.684-32.478h-135.41zm411.87 0-66.634 313.53h80.999l66.4-313.53h-80.765zm451.76 0c-19.532 0-29.88 10.457-37.474 28.73l-118.67 284.8h84.942l16.434-47.467h103.48l9.9931 47.467h74.948l-65.385-313.53h-68.273zm11.047 84.707 25.178 117.65h-67.454l42.276-117.65z")

    def update_info(self, card: ModelCardNumber):
        # update brand logo
        self.show_brand(card.number.brand)
        # update card info
        self.number.text = card.number.masked
        self.holder.text = card.holder
        self.expires.text = card.expires.strftime("%m/%y")
        self.cvc.text = card.cvc


class FieldBankCard(justpy.Form):
    _layout_class = "w-full md:w-full lg:w-9/12 mx-auto md:mx-0"
    _container_class = "bg-white p-10 flex flex-col w-full shadow-xl rounded-xl"
    _group_class = "flex flex-col w-full my-5"
    _expires_group_class = "flex flex-col block  space-x-4"
    _label_class = "text-gray-500 mb-2 uppercase"
    _input_class = "appearance-none border-2 border-gray-100 rounded-lg px-4 py-3 placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-green-600 focus:shadow-lg"
    _select_class = "w-32 text-xl m-4 p-2 bg-white  border rounded"

    def __init__(self, **kwargs):
        """
        widgets:
        - container
        - holder
        - number
        - expires
        - cvc
        - snapshot
        """
        # handle parameters
        params = {w: kwargs.pop(f"_{w}", dict()) for w in [
            "container", "holder", "number", "expires", "cvc", "snapshot"]}

        self.with_snapshot = kwargs.pop("with_snapshot", True)
        self.card = ModelCardNumber(
                        holder="John Doe",
                        number="4242424242424242",
                        expires="2022-08-01",
                        cvc="999")

        # layout
        args_default(kwargs, {"classes": FieldBankCard._layout_class})
        super().__init__(**kwargs)

        # container
        args_default(params["container"],
                {"a": self,
                 "classes": FieldBankCard._container_class})
        c = justpy.Div(**params["container"])

        # form
        f = justpy.Form(a=c, classes="w-full")

        # number group
        args_default(params["number"],
                {"a": f,
                 "name": "number",
                 "error": False,
                 "autofocus": True,
                 "label": "Card number",
                 "hint": "Please insert card number",
                 "hide-hint": True,
                 "clearable": True,
                 "outlined": True,
                 "input-class": FieldBankCard._input_class,
                 "rounded": True})
        self.number = justpy.QInput(**params["number"])
        self.number.on("input", self.change_number)

        # holder group
        args_default(params["holder"],
                {"a": f,
                 "name": "holder",
                 "error": False,
                 "autofocus": False,
                 "label": "Holder name",
                 "hint": "Please insert holder name",
                 "hide-hint": True,
                 "clearable": True,
                 "outlined": True,
                 "input-class": FieldBankCard._input_class,
                 "rounded": True})
        self.holder = justpy.QInput(**params["holder"])
        self.holder.on("input", self.change_holder)

        # exp group
        eg = justpy.Div(a=f, classes=FieldBankCard._expires_group_class)
        args_default(params["expires"],
                {"a": eg,
                 "label": "Month",
                 "hint": "Please select the month of expires",
                 "hide-hint": True,
                 "outlined": True,
                 "rounded": True,
                 "options": ["01", "02", "03", "04", "05", "06",
                    "07", "08", "09", "10", "11", "12"],
                 "value": "01"
                 })
        justpy.QSelect(**params["expires"])


        thisyear = datetime.now().strftime("%Y")
        params["expires"].update({"a": eg,
                 "label": "Year",
                 "hint": "Please select the year of expires",
                 "options": [str(int(thisyear) + step) for step in range(10)],
                 "value": thisyear})
        justpy.QSelect(**params["expires"])

        # cvc group
        args_default(params["cvc"],
                {"a": f,
                 "name": "cvc",
                 "error": False,
                 "autofocus": False,
                 "label": "CVC",
                 "hint": "Please insert 3 digits CVC",
                 "hide-hint": True,
                 "outlined": True,
                 "clearable": True,
                 "input-class": FieldBankCard._input_class,
                 "rounded": True})
        self.cvc = justpy.QInput(**params["cvc"])
        self.cvc.on("input", self.change_cvc)

        if self.with_snapshot:
            # snapshot container
            sg = justpy.Div(a=self)
            args_default(params["snapshot"], {"a": sg})
            self.snapshot = FieldBankCardSnapshot(**params["snapshot"])

        self.notification = justpy.QNotify(a=self, position="bottom",
                                closeBtn='Close', timeout=3000)

    async def change_number(self, msg):
        if len(msg.target.value) < 11:
            self.number.error= False
            return
        try:
            self.card.number = msg.target.value
            self.snapshot.update_info(self.card)
        except ValueError as e:
            ui_input_error(self.number, f"{e}")

    async def change_holder(self, msg):
        self.holder.error = False
        try:
            self.card.holder = msg.target.value
            self.snapshot.update_info(self.card)
        except ValueError as e:
            ui_input_error(self.holder, f"{e}")


    async def change_expires(self, msg):
        try:
            self.card.expires = f"{self.year.value}-{self.month.value}-01"
            self.snapshot.update_info(self.card)
        except ValueError as e:
            ui_notify(self, message=f"{e}")

    async def change_cvc(self, msg):
        self.cvc.error = False
        try:
            self.card.cvc = msg.target.value
            self.snapshot.update_info(self.card)
        except ValueError as e:
            ui_input_error(self.cvc, f"{e}")
