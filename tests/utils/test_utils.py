#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-08-09 20:07:43
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-10 00:15:27
* @FilePath    : /guanfu/tests/utils/test_utils.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''

import pytest

from guanfu.utils.rightsmap import RightsMap

@pytest.fixture(scope="function")
def clear_rights_map():
    RightsMap.__items__ = None
    RightsMap.__dimentions__ = None
    RightsMap.__rights_map__ = None

@pytest.mark.usefixtures("clear_rights_map")
def test_init0():
    rm = RightsMap(bins=int("010011000001101", 2))
    assert isinstance(rm, RightsMap)
    assert not rm.__items__
    assert not rm.__dimentions__
    assert not rm.__rights_map__
    assert rm.__rights_val__ == 9741

@pytest.mark.usefixtures("clear_rights_map")
def test_init1():
    rm = RightsMap(
        bins=int("010011000001101", 2),
        rights={ "items": ["I1A1", "I1A2", "I1A3", "I2A1", "I2A2", "I1A1", "I1A2"],
                 "dimens": ["read", "update", "release"]})
    assert isinstance(rm, RightsMap)
    assert rm.__items__ == ["I1A1", "I1A2", "I1A3", "I2A1", "I2A2"]
    assert rm.__dimentions__ == ["read", "update", "release"]
    assert rm.__rights_map__["read@I1A1"] == 0
    assert rm.__rights_val__ == 9741

@pytest.mark.usefixtures("clear_rights_map")
def test_init2():
    with pytest.raises(ValueError) as e:
        rm = RightsMap(rights={
            "items": ["I1A1", "I1A2", "I1A3", "I2A1", "I2A2"]})

@pytest.mark.usefixtures("clear_rights_map")
def test_init3():
    with pytest.raises(ValueError) as e:
        rm = RightsMap(rights={
            "dimens": ["read", "update", "release"]})

@pytest.mark.usefixtures("clear_rights_map")
def test_init4():
    rm = RightsMap(rights={}, bins=None)
    assert isinstance(rm, RightsMap)
    assert not rm.__items__
    assert not rm.__dimentions__
    assert not rm.__rights_map__
    assert rm.__rights_val__ == 0

@pytest.fixture(scope="function")
def preamble():
    return RightsMap(
        bins=int("010011000001101", 2),
        rights={ "items": ["I1A1", "I1A2", "I1A3", "I2A1", "I2A2"],
                 "dimens": ["read", "update", "release"]})

def test_as_int(preamble):
    assert int(preamble) == 9741

def test_and(preamble):
    res = preamble & int("111111111111011", 2)
    assert int(res) == 9737
    preamble &= int("111111111111011", 2)
    assert int(preamble) == 9737

def test_or(preamble):
    res = preamble | int("10", 2)
    assert int(res) == 9743
    preamble |= int("10", 2)
    assert int(preamble) == 9743

def test_xor(preamble):
    res = preamble ^ int("010011000001100", 2)
    assert int(res) == 1
    preamble ^= int("010011000001100", 2)
    assert int(preamble) == 1

def test_len(preamble):
    assert len(preamble) == len(["I1A1", "I1A2", "I1A3", "I2A1", "I2A2"])

def test_contain(preamble):
    for e in ["I1A1", "I1A2", "I1A3", "I2A1", "I2A2"]:
        assert e in preamble

    assert not "not exist" in preamble

def test_get(preamble):
    assert preamble["I1A1"] == {"read": True, "update": False, "release": True}
    assert preamble["I2A2"] == {"read": False, "update": True, "release": False}

def test_iter(preamble):
    assert list(preamble)[0] == [
        ("read@I1A1", True),
        ("update@I1A1", False),
        ("release@I1A1", True)]
    assert list(preamble)[-1] == [
        ("read@I2A2", False),
        ("update@I2A2", True),
        ("release@I2A2", False)]

def test_to_bits(preamble):
    assert preamble.to_bits() == bin(int("010011000001101", 2))
    assert preamble.to_bits() == "0b10011000001101"

def test_get_items_rights(preamble):
    res = preamble.get_items_rights(["I1A3", "not existed", "I2A1"])
    assert "not existed" not in res.keys()
    assert res["I1A3"] == {"read": False, "update": False, "release": False}
    assert res["I2A1"] == {"read": True, "update": True, "release": False}


def test_get_items_with_rights(preamble):
    res = preamble.get_items_with_rights(["read", "not existed", "release"])
    assert "not existed" not in res.keys()
    assert res["read"] == ["I1A1", "I1A2", "I2A1"]
    assert res["release"] == ["I1A1"]

def test_set_rights(preamble):
    assert not preamble.set_item_rights("I2A1", ["update", "not existed", "release"])
    assert preamble.set_item_rights("I2A1", ["update", "release"])
    assert preamble.test_item_right("I2A1", "update")
    assert preamble.test_item_right("I2A1", "release")
    res = preamble.get_items_rights(["I1A3", "not existed", "I2A1"])
    assert "not existed" not in res.keys()
    assert res["I1A3"] == {"read": False, "update": False, "release": False}
    assert res["I2A1"] == {"read": True, "update": True, "release": True}

def test_clear_rights(preamble):
    assert not preamble.clear_item_rights("I2A1", ["update", "not existed", "release"])
    assert preamble.clear_item_rights("I2A1", ["update", "release"])
    assert not preamble.test_item_right("I2A1", "update")
    assert not preamble.test_item_right("I2A1", "release")
    res = preamble.get_items_rights(["I1A3", "not existed", "I2A1"])
    assert "not existed" not in res.keys()
    assert res["I1A3"] == {"read": False, "update": False, "release": False}
    assert res["I2A1"] == {"read": True, "update": False, "release": False}
