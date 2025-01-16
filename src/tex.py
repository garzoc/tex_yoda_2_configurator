#!/usr/bin/env python3
from enum import Enum
from TexConfig import TexProfile, TexLayer, TexFnLayer, TexConfigurator

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
        texBuilder = TexBinaryBuilder(shura)
        texBuilder.binaryGenerate("KEYMAP.TEX")

    if config == BoardConfig.SHINOBI:
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
        texBuilder = TexBinaryBuilder(shinobi)
        texBuilder.binaryGenerate("KEYMAP.TEX")

    if config == BoardConfig.YODA2:
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
        texBuilder = TexBinaryBuilder(yoda2)
        texBuilder.binaryGenerate("KEYMAP.TEX")


if __name__ == "__main__":
    init()
