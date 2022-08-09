#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-09 11:28:28
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-10 00:16:01
* @FilePath    : /guanfu/guanfu/utils/rightsmap.py
* @Description : manipulate rigts with bitmap
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from optparse import Option
from typing import Optional


class RightsMap(object):
    __rights_map__: dict = None
    __items__: set = None
    __dimentions__: set = None


    @classmethod
    def load_rights_def(cls, rights_def: dict) -> None:
        '''
        * @description : load rights definition from a dict with:
            |    key    |                value                  |
            |  items    | item name in list                     |
            | dimens    | dimensions name for each right in list|
          example:
            {"items": ["type1.attr1", "type1.attr2", "typeX.attrX"],
             "dimens": ["read", "change", "review", "release"]}
        * @param        {*} cls
        * @param        {dict} rights_def rights definition
        * @return       {*}
        '''
        print(f"====load rights def")
        if not rights_def:
            raise ValueError(f"right map load def failed with empty defs")

        if not rights_def.get("items", None):
            raise ValueError(f"right map load def failed without key 'items'")

        if not rights_def.get("dimens", None):
            raise ValueError(f"right map load def failed without key 'dimens'")
        RightsMap.__items__ = list(set(rights_def["items"]))
        RightsMap.__items__.sort(key=rights_def["items"].index)
        RightsMap.__dimentions__ = list(set(rights_def["dimens"]))
        RightsMap.__dimentions__.sort(key=rights_def["dimens"].index)
        i = 0
        RightsMap.__rights_map__ = dict()
        for r in RightsMap.__items__:
            for d in RightsMap.__dimentions__:
                RightsMap.__rights_map__[f"{d}@{r}"] = i
                i += 1

    def __init__(self,
                 bins: Optional[int] = 0,
                 rights: Optional[dict] = None) -> object:
        '''
        * @description : construct a RightMap object with zero or another value
        * @param        {*} self
        * @param        {Optional} bins   - binary string
        * @param        {Optional} rights - rights def in dict
        * @return       {*}
        '''
        if bins:
            self.__rights_val__ = int(bins)
        else:
            self.__rights_val__ = 0

        if rights and not RightsMap.__rights_map__:
            RightsMap.load_rights_def(rights)


    def __int__(self) -> int:
        '''
        * @description : convert to int
        * @param        {*} self
        * @return       {*}
        '''
        return self.__rights_val__


    def __and__(self, other) -> object:
        '''
        * @description : r1 = r0 & mask
        * @param        {*} self
        * @param        {*} other
        * @return       {*} new object
        '''
        if isinstance(other, int) or isinstance(other, RightsMap):
            return RightsMap(bins = (self.__rights_val__ & int(other)))
        else:
            return None


    def __or__(self, other) -> object:
        '''
        * @description : r1 = r0 | mask
        * @param        {*} self
        * @param        {*} other
        * @return       {*} new object
        '''
        if isinstance(other, int) or isinstance(other, RightsMap):
            return RightsMap(bins = (self.__rights_val__ | int(other)))
        else:
            return None


    def __xor__(self, other) -> object:
        '''
        * @description : r1 = r0 ^ mask
        * @param        {*} self
        * @param        {*} other
        * @return       {*} new object
        '''
        if isinstance(other, int) or isinstance(other, RightsMap):
            return RightsMap(bins = (self.__rights_val__ ^ int(other)))
        else:
            return None


    def __iand__(self, other) -> object:
        '''
        * @description : r1 &= mask
        * @param        {*} self
        * @param        {*} other
        * @return       {*} object itself changed
        '''
        if isinstance(other, int) or isinstance(other, RightsMap):
            self.__rights_val__ &= int(other)
            return self
        else:
            raise ValueError(f"can't &= with {other}")


    def __ior__(self, other) -> object:
        '''
        * @description : r1 |= mask
        * @param        {*} self
        * @param        {*} other
        * @return       {*} object itself changed
        '''
        if isinstance(other, int) or isinstance(other, RightsMap):
            self.__rights_val__ |= int(other)
            return self
        else:
            raise ValueError(f"can't |= with {other}")


    def __ixor__(self, other) -> object:
        '''
        * @description : r1 ^= mask
        * @param        {*} self
        * @param        {*} other
        * @return       {*} object itself changed
        '''
        if isinstance(other, int) or isinstance(other, RightsMap):
            self.__rights_val__ ^= int(other)
            return self
        else:
            raise ValueError(f"can't ^= with {other}")


    def __len__(self) -> int:
        return len(RightsMap.__items__) if RightsMap.__items__ else 0


    def __getitem__(self, key) -> Optional[dict]:
        if not key:
            return None

        if not RightsMap.__items__ or not RightsMap.__dimentions__:
            return None

        return {d: (self.__rights_val__ & \
                            (1 << RightsMap.__rights_map__[f"{d}@{key}"])) > 0 \
                        for d in RightsMap.__dimentions__}


    def __contains__(self, item) -> bool:
        return item in RightsMap.__items__


    def __iter__(self):
        return [[(f"{d}@{r}", (self.__rights_val__ & \
                        (1 << RightsMap.__rights_map__[f"{d}@{r}"])) > 0) \
                    for d in RightsMap.__dimentions__]
                for r in RightsMap.__items__].__iter__()


    def to_bits(self) -> str:
        '''
        * @description : return binary string
        * @param        {*} self
        * @return       {*}
        '''
        return bin(self.__rights_val__)


    def get_items_rights(self, items: list) -> Optional[dict]:
        '''
        * @description : get rights of specified items
        * @param        {*} self
        * @param        {list} items
        * @return       {*} like {"type1.attr1": {"read": True, "release": False}}
        '''
        if not items:
            return None

        if not RightsMap.__items__ or not RightsMap.__dimentions__:
            return None

        res = dict()
        for item in set(items):
            if not item in RightsMap.__items__:
                continue
            else:
                res[item] = {d: (self.__rights_val__ & \
                                (1 << RightsMap.__rights_map__[f"{d}@{item}"])) > 0 \
                            for d in RightsMap.__dimentions__}
        return res


    def get_items_with_rights(self, dimens: list) -> Optional[dict]:
        '''
        * @description : get items with specified rights
        * @param        {*} self
        * @param        {list} dimens
        * @return       {*} like {"read": ["type1.attr1", "type2.attr1"],
                                  "release": ["type1.attr1"]}}
        '''
        if not dimens:
            return None

        if not RightsMap.__items__ or not RightsMap.__dimentions__:
            return None

        res = dict()
        for d in set(dimens):
            if not d in RightsMap.__dimentions__:
                continue
            else:
                res[d] = [r for r in RightsMap.__items__ if (self.__rights_val__ & \
                                (1 << RightsMap.__rights_map__[f"{d}@{r}"])) > 0]
        return res


    def set_item_rights(self, item: str, dimens: list) -> bool:
        '''
        * @description : set specified item withold specified dimensions right
        * @param        {*} self
        * @param        {str} item
        * @param        {list} dimens
        * @return       {*}
        '''
        if not dimens:
            return True

        if not item in RightsMap.__items__:
            return False

        if (set(dimens) - set(RightsMap.__dimentions__)):
            # there is something out of dimensions
            return False

        for d in dimens:
            self.__rights_val__ |= (1 << RightsMap.__rights_map__[f"{d}@{item}"])
        return True


    def clear_item_rights(self, item: str, dimens: list) -> bool:
        '''
        * @description : clear specified item with specified dimensions right
        * @param        {*} self
        * @param        {str} item
        * @param        {list} dimens
        * @return       {*}
        '''
        if not dimens:
            return True

        if not item in RightsMap.__items__:
            return False

        if (set(dimens) - set(RightsMap.__dimentions__)):
            # there is something out of dimensions
            return False

        for d in dimens:
            self.__rights_val__ &= \
                (~(1 << RightsMap.__rights_map__[f"{d}@{item}"]))
        return True


    def test_item_right(self, item: str, dimension: str) -> bool:
        '''
        * @description : test if the right settled
        * @param        {*} self
        * @param        {str} item
        * @param        {str} dimension
        * @return       {*}
        '''
        if not item in RightsMap.__items__ or \
            not dimension in RightsMap.__dimentions__:
            return False
        return self.__rights_val__ & \
            (1 << RightsMap.__rights_map__[f"{dimension}@{item}"]) > 0
