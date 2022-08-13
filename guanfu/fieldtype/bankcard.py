#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-12 16:11:03
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-13 13:21:31
* @FilePath    : /guanfu/guanfu/fieldtype/bankcard.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import justpy
from datetime import date, datetime
from pydantic import BaseModel
from pydantic.types import PaymentCardNumber, PaymentCardBrand, constr


# cardnumber
# name
# cvv
# exp date
# snapshot: brand, card mask, ...

class ModelCardNumber(BaseModel):
    holder: constr(strip_whitespace=True, min_length=1)
    number: PaymentCardNumber
    expires: date
    cvc: constr(strip_whitespace=True, regex="[0-9]{3}")

    class Config:
        validate_assignment = True


class FieldBankCardSnapshot(justpy.Figure):
    _card_class = "w-max h-max relative select-none pointer-events-none"
    _verso_class = "z-1 absolute overflow-hidden transform translate-y-12 left-16 w-96 h-56 rounded-2xl bg-gray-100 shadow-2xl"
    _verso_bar_class = "w-full h-12 bg-gray-200 absolute top-10"
    _recto_class = "z-2 absolute overflow-hidden w-96 h-56 rounded-2xl px-8 py-6 bg-red-400 text-white shadow-xl flex flex-col justify-end gap-6"
    _logo_class = "absolute top-6 right-8 w-16 h-8 flex justify-items-center items-center"
    _chip_class = "w-11 h-7 rounded bg-yellow-100"
    _number_class = "whitespace-nowrap text-2xl font-semibold"
    _info_class = "flex gap-8"
    _info_group_class = "flex flex-col w-max"
    _info_lable_class = "text-xs uppercase"
    _info_text_class = "whitespace-nowrap text-lg"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # figure
        self.classes = kwargs.get(
            "figure_class",
            "w-full") # "top-8 left-8")

        # card div
        cd = justpy.Div(a=self,
                        classes=kwargs.get(
                            "card_class",
                            FieldBankCardSnapshot._card_class))

        # verso
        verso = justpy.Div(a=cd,
                           classes=kwargs.get(
                                "verso_class",
                                FieldBankCardSnapshot._verso_class))
        justpy.Div(a=verso,
                   classes=kwargs.get(
                        "verso_bar_class",
                        FieldBankCardSnapshot._verso_bar_class),
                   text=kwargs.get(
                        "verso_bar_text",
                        "&nbsp;"))

        # recto
        rd = justpy.Div(a=cd,
                        classes=kwargs.get(
                            "recto_class",
                            FieldBankCardSnapshot._recto_class))
        #logo
        ld = justpy.Div(a=rd,
                        classes=kwargs.get(
                            "logo_class",
                            FieldBankCardSnapshot._logo_class))
        self.logo = justpy.Svg(a=ld, viewBox="0 0 1000 324.68")
        # visa logo
        self.show_brand(brand=kwargs.get("card_brand", PaymentCardBrand.visa))
        if kwargs.get("with_chip", True):
            justpy.Div(a=rd,
                       classes=kwargs.get(
                            "chip_class",
                            FieldBankCardSnapshot._chip_class),
                       text="  ")
        # number
        self.number = justpy.Div(a=rd,
                                 classes=kwargs.get(
                                    "number_class",
                                    FieldBankCardSnapshot._number_class),
                                 style=kwargs.get(
                                    "number_style",
                                    "font-family:Courier new, mono;"),
                                 text=kwargs.get(
                                    "card_number",
                                    "424242******4242"))
        # info
        # - holder
        nd = justpy.Div(a=rd,
                        classes=kwargs.get(
                            "info_class",
                            FieldBankCardSnapshot._info_class))
        hd = justpy.Div(a=nd,
                        classes=kwargs.get(
                            "info_group_class",
                            FieldBankCardSnapshot._info_group_class))
        # -- label
        justpy.Span(a=hd,
                    classes=kwargs.get(
                        "info_label_class",
                        FieldBankCardSnapshot._info_lable_class),
                    text=kwargs.get(
                        "holder_label",
                        "Card holder"))
        # -- name
        self.holder = justpy.Span(a=hd,
                                classes=kwargs.get(
                                    "info_text_class",
                                    FieldBankCardSnapshot._info_text_class),
                                text=kwargs.get(
                                    "holder_text",
                                    "John Doe"))
        # - expires
        ed = justpy.Div(a=nd,
                        classes=kwargs.get(
                            "info_group_class",
                            FieldBankCardSnapshot._info_group_class))
        # -- label
        justpy.Span(a=ed,
                    classes=kwargs.get(
                        "info_label_class",
                        FieldBankCardSnapshot._info_lable_class),
                    text=kwargs.get(
                        "expires_label",
                        "Expires"))
        # -- date
        self.expires = justpy.Span(a=ed,
                                   classes=kwargs.get(
                                        "info_text_class",
                                        FieldBankCardSnapshot._info_text_class),
                                   text=kwargs.get(
                                        "expires_text",
                                        "09/28"))
        # - cvc
        vd = justpy.Div(a=nd,
                        classes=kwargs.get(
                            "info_group_class",
                            FieldBankCardSnapshot._info_group_class))
        # -- label
        justpy.Span(a=vd,
                    classes=kwargs.get(
                        "info_label_class",
                        FieldBankCardSnapshot._info_lable_class),
                    text=kwargs.get(
                        "cvc_label",
                        "cvc"))
        # -- cvc
        self.cvc = justpy.Span(a=vd,
                               classes=kwargs.get(
                                    "info_text_class",
                                    FieldBankCardSnapshot._info_text_class),
                               text=kwargs.get(
                                    "cvc_text",
                                    "123"))

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
    _expires_group_class = "block  space-x-4"
    _label_class = "text-gray-500 mb-2 uppercase"
    _input_class = "appearance-none border-2 border-gray-100 rounded-lg px-4 py-3 placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-green-600 focus:shadow-lg"
    _select_class = "w-32 text-xl m-4 p-2 bg-white  border rounded"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.with_snapshot = kwargs.get("with_snapshot", True)
        self.card = ModelCardNumber(
                        holder="John Doe",
                        number="4242424242424242",
                        expires="2022-08-01",
                        cvc="999")

        # layout
        self.classes = kwargs.get(
            "layout_class",
            FieldBankCard._layout_class)

        # container
        c = justpy.Div(a=self,
                       classes=kwargs.get(
                            "container_class",
                            FieldBankCard._container_class))

        # form
        f = justpy.Form(a=c, classes="w-full")

        # number group
        ug = justpy.Div(a=f,
                        classes=kwargs.get(
                            "group_class",
                            FieldBankCard._group_class))
        justpy.Label(a=ug,
                     classes=kwargs.get(
                            "label_class",
                            FieldBankCard._label_class),
                     text=kwargs.get(
                            "number_lable",
                            "Card number"))
        iu = justpy.Input(a=ug,
                          classes=kwargs.get(
                                "input_class",
                                FieldBankCard._input_class),
                          placeholder=kwargs.get(
                                "number_placeholder",
                                "Please insert card number"))
        iu.on("input", self.change_number)

        # holder group
        ag = justpy.Div(a=f,
                        classes=kwargs.get(
                            "group_class",
                            FieldBankCard._group_class))
        justpy.Label(a=ag,
                     classes=kwargs.get(
                            "label_class",
                            FieldBankCard._label_class),
                     text=kwargs.get(
                            "holder_lable",
                            "Holder name"))
        ia = justpy.Input(a=ag,
                           classes=kwargs.get(
                                "input_class",
                                FieldBankCard._input_class),
                           placeholder=kwargs.get(
                                "holder_name",
                                "Please insert holder name"))
        ia.on("input", self.change_holder)

        # exp group
        eg = justpy.Div(a=f,
                        classes=kwargs.get(
                            "expires_group_class",
                            FieldBankCard._expires_group_class))
        justpy.Label(a=eg,
                     classes=kwargs.get(
                            "label_class",
                            FieldBankCard._label_class),
                     text=kwargs.get(
                            "expires_month_lable",
                            "Month"))
        self.month = justpy.Select(a=eg,
                                   classes=kwargs.get(
                                        "select_class",
                                        FieldBankCard._select_class),
                                   value="01",
                                   change=self.change_expires)
        for mon in ["01", "02", "03", "04", "05", "06",
                    "07", "08", "09", "10", "11", "12"]:
            self.month.add(justpy.Option(value=mon, text=mon))

        justpy.Label(a=eg,
                     classes=kwargs.get(
                            "label_class",
                            FieldBankCard._label_class),
                     text=kwargs.get(
                            "expires_year_lable",
                            "Year"))
        thisyear = datetime.now().strftime("%Y")
        self.year = justpy.Select(a=eg,
                                  classes=kwargs.get(
                                        "select_class",
                                        FieldBankCard._select_class),
                                  value=thisyear,
                                  change=self.change_expires)
        for step in range(10):
            year = str(int(thisyear) + step)
            self.year.add(justpy.Option(value=year, text=year))

        # cvc group
        cg = justpy.Div(a=f,
                        classes=kwargs.get(
                            "group_class",
                            FieldBankCard._group_class))
        justpy.Label(a=cg,
                     classes=kwargs.get(
                            "label_class",
                            FieldBankCard._label_class),
                     text=kwargs.get(
                            "cvc_lable",
                            "cvc"))
        ic = justpy.Input(a=cg,
                          classes=kwargs.get(
                                "input_class",
                                FieldBankCard._input_class),
                          placeholder=kwargs.get(
                                "cvc_placeholder",
                                "Please insert 3 digits CVC"))
        ic.on("input", self.change_cvc)

        if self.with_snapshot:
            # snapshot container
            sg = justpy.Div(a=self)
            kwargs['a'] = sg
            self.snapshot = FieldBankCardSnapshot(**kwargs)

    async def change_number(self, msg):
        if len(msg.target.value) < 11:
            return
        try:
            self.card.number = msg.target.value
        except Exception as e:
            # TODO collect and response error to UI
            print(f"!!!!{e}")
        self.snapshot.update_info(self.card)

    async def change_holder(self, msg):
        try:
            self.card.holder = msg.target.value
        except Exception as e:
            # TODO collect and response error to UI
            print(f"!!!!{e}")
        self.snapshot.update_info(self.card)

    async def change_expires(self, msg):
        try:
            self.card.expires = f"{self.year.value}-{self.month.value}-01"
        except Exception as e:
            # TODO collect and response error to UI
            print(f"!!!!{e}")
        self.snapshot.update_info(self.card)

    async def change_cvc(self, msg):
        try:
            self.card.cvc = msg.target.value
        except Exception as e:
            # TODO collect and response error to UI
            print(f"!!!!{e}")
        self.snapshot.update_info(self.card)
