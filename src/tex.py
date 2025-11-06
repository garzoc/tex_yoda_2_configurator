#!/usr/bin/env python3
from enum import Enum
from TexConfig import TexProfile, TexLayer, TexFnLayer, TexConfigurator, TexMacroOp, TexMacro

from TexConfig.yoda2 import TexConfiguratorYoda2
from TexConfig.shura import TexConfiguratorShura
from TexConfig.shinobi import TexConfiguratorShinobi
from TexConfig.binary import TexBinaryBuilder


class BoardConfig(Enum):
    SHURA = 0
    SHINOBI = 1
    YODA2 = 2


def init():
    yoda2: TexConfigurator = TexConfiguratorYoda2()
    shura: TexConfigurator = TexConfiguratorShura()
    shinobi: TexConfigurator = TexConfiguratorShinobi()

    config = BoardConfig.SHURA

    if config == BoardConfig.SHURA:
        # shura.addMacroOp(TexMacro.MACRO_1, TexMacroOp.DOWN, "3")
        # shura.addMacroOp(TexMacro.MACRO_1, TexMacroOp.UP, "3")
        # shura.addMacroOp(TexMacro.MACRO_2, TexMacroOp.DOWN, "4")
        # shura.addMacroOp(TexMacro.MACRO_2, TexMacroOp.UP, "4")

        # Binding Shura's fn key to fn layer 2, disables the caps-lock functionally
        # binding to layer1 will keep the functionality
        shura.addConfigFnEntry(TexProfile.PROFILE_1, TexFnLayer.FN_LAYER2, "fn")
        shura.addConfigFnEntry(TexProfile.PROFILE_1, TexFnLayer.FN_LAYER2, "right_shift")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "e", "vol+")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "left", "home")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "right", "end")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "up", "pageUp")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "down", "pageDown")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "k", "up")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "m", "left")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "l", "right")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, ",", "down")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "w", "right_shift")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "q", "right_control")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "e", "b")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "tab", "capslock")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "left_mouse", "`")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "esc", "`")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "p", "play/pause")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "n", "next")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "b", "prev")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "backspace", "del")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "1", "f1")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "2", "f2")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "3", "f3")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "4", "f4")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "5", "f5")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "6", "f6")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "7", "f7")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "8", "f8")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "9", "f9")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "0", "f10")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "-", "f11")
        shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "=", "f12")
        texBuilder = TexBinaryBuilder(shura)
        texBuilder.binaryGenerate("KEYMAP.TEX")

    if config == BoardConfig.SHINOBI:
        shinobi.addConfigFnEntry(TexProfile.PROFILE_1, TexFnLayer.FN_LAYER2, "fn")
        shinobi.addConfigFnEntry(TexProfile.PROFILE_1, TexFnLayer.FN_LAYER2, "right_shift")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "e", "vol+")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "left", "home")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "right", "end")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "up", "pageUp")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "down", "pageDown")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "k", "up")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "m", "left")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "l", "right")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, ",", "down")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "w", "right_shift")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "q", "right_control")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "e", "b")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "tab", "capslock")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "left_mouse", "`")
        shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "esc", "`")
        texBuilder = TexBinaryBuilder(shinobi)
        texBuilder.binaryGenerate("KEYMAP.TEX")

    if config == BoardConfig.YODA2:
        yoda2.addConfigFnEntry(TexProfile.PROFILE_1, TexFnLayer.FN_LAYER2, "capslock")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "e", "vol+")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.NORMAL, "right_shift", "up")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.NORMAL, "right_control", "right")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.NORMAL, "right_alt", "left")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.NORMAL, "right_win", "down")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "right_shift", "pageUp")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "right_win", "pageDown")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "right_alt", "home")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "right_control", "end")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "esc", "`")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "tab", "capslock")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "p", "play/pause")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "n", "next")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "b", "prev")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "left_mouse", "`")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "backspace", "del")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "1", "f1")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "2", "f2")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "3", "f3")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "4", "f4")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "5", "f5")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "6", "f6")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "7", "f7")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "8", "f8")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "9", "f9")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "0", "f10")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "-", "f11")
        yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.FN2, "=", "f12")
        texBuilder = TexBinaryBuilder(yoda2)
        texBuilder.binaryGenerate("KEYMAP.TEX")


if __name__ == "__main__":
    init()
