from typing import Generator, Any
from TexConfig import TexProfile, TexLayer, TexFnLayer, TexConfBinding, TexConfigurator


class TexConfiguratorYoda2(TexConfigurator):
    keybindings = [
        TexConfBinding("a", 0x0400, 0x34, True),  # 00000100: 00110100
        TexConfBinding("b", 0x0500, 0x01, True),  # 00000101: 00000001
        TexConfBinding("c", 0x0600, 0x32, True),  # 00000110: 00110010
        TexConfBinding("d", 0x0700, 0x03, True),  # 00000111: 00000011
        TexConfBinding("e", 0x0800, 0x15, True),  # 00001000: 00010101
        TexConfBinding("f", 0x0900, 0x0b, True),  # 00001001: 00001011
        TexConfBinding("g", 0x0a00, 0x13, True),
        TexConfBinding("h", 0x0b00, 0x1b, True),
        TexConfBinding("i", 0x0c00, 0x3d, True),
        TexConfBinding("j", 0x0d00, 0x23, True),
        TexConfBinding("k", 0x0e00, 0x2b, True),
        TexConfBinding("l", 0x0f00, 0x33, True),
        TexConfBinding("m", 0x1000, 0x11, True),
        TexConfBinding("n", 0x1100, 0x09, True),
        TexConfBinding("o", 0x1200, 0x04, True),
        TexConfBinding("p", 0x1300, 0x0c, True),
        TexConfBinding("q", 0x1400, 0x05, True),
        TexConfBinding("r", 0x1500, 0x1d, True),
        TexConfBinding("s", 0x1600, 0x3c, True),
        TexConfBinding("t", 0x1700, 0x25, True),
        TexConfBinding("u", 0x1800, 0x35, True),
        TexConfBinding("v", 0x1900, 0x3a, True),
        TexConfBinding("w", 0x1a00, 0x0d, True),
        TexConfBinding("x", 0x1b00, 0x2a, True),
        TexConfBinding("y", 0x1c00, 0x2d, True),
        TexConfBinding("z", 0x1d00, 0x22, True),
        TexConfBinding("1", 0x1e00, 0x0f, True),
        TexConfBinding("2", 0x1f00, 0x17, True),
        TexConfBinding("3", 0x2000, 0x1f, True),
        TexConfBinding("4", 0x2100, 0x27, True),
        TexConfBinding("5", 0x2200, 0x2f, True),
        TexConfBinding("6", 0x2300, 0x37, True),
        TexConfBinding("7", 0x2400, 0x3f, True),
        TexConfBinding("8", 0x2500, 0x06, True),
        TexConfBinding("9", 0x2600, 0x0e, True),
        TexConfBinding("0", 0x2700, 0x16, True),
        TexConfBinding("enter", 0x2800, 0x0a, True),
        TexConfBinding("esc", 0x2900, 0x07, True),
        TexConfBinding("backspace", 0x2a00, 0x36, True),
        TexConfBinding("tab", 0x2b00, 0x3e, True),
        TexConfBinding("spacebar", 0x2c00, 0x18, True),
        TexConfBinding("-", 0x2d00, 0x1e, True),
        TexConfBinding("=", 0x2e00, 0x26, True),
        TexConfBinding("[", 0x2f00, 0x14, True),
        TexConfBinding("]", 0x3000, 0x1c, True),
        TexConfBinding("\\", 0x3100, 0x24, True),
        TexConfBinding(";", 0x3300, 0x3b, True),
        TexConfBinding("'", 0x3400, 0x02, True),
        TexConfBinding("`", 0x3500, 0x2e, False),  # Can be enabled in DIY config split backspace
        TexConfBinding(",", 0x3600, 0x19, True),
        TexConfBinding(".", 0x3700, 0x21, True),
        TexConfBinding("/", 0x3800, 0x29, True),
        TexConfBinding("capslock", 0x3900, 0x2c, True),
        TexConfBinding("f1", 0x3a00, 0, False),
        TexConfBinding("f2", 0x3b00, 0, False),
        TexConfBinding("f3", 0x3c00, 0, False),
        TexConfBinding("f4", 0x3d00, 0, False),
        TexConfBinding("f5", 0x3e00, 0, False),
        TexConfBinding("f6", 0x3f00, 0, False),
        TexConfBinding("f7", 0x4000, 0, False),
        TexConfBinding("f8", 0x4100, 0, False),
        TexConfBinding("f9", 0x4200, 0, False),
        TexConfBinding("f10", 0x4300, 0, False),
        TexConfBinding("f11", 0x4400, 0, False),
        TexConfBinding("f12", 0x4500, 0, False),
        TexConfBinding("PrtSc", 0x4600, 0, False),
        TexConfBinding("ScrLk", 0x4700, 0, False),
        TexConfBinding("pause", 0x4800, 0, False),
        TexConfBinding("ins", 0x4900, 0, False),
        TexConfBinding("home", 0x4a00, 0, False),
        TexConfBinding("pageUp", 0x4b00, 0, False),
        TexConfBinding("del", 0x4c00, 0, False),
        TexConfBinding("end", 0x4d00, 0, False),
        TexConfBinding("pageDown", 0x4e00, 0, False),
        TexConfBinding("left", 0x5000, 0, False),
        TexConfBinding("down", 0x5100, 0, False),
        TexConfBinding("up", 0x5200, 0, False),
        TexConfBinding("left_mouse", 0xc800, 0x45, True),  # Can this value be bound to another key?
        TexConfBinding("middle_mouse", 0xc900, 0x46, True),  # Does rebinding change the default scroll behavior?
        TexConfBinding("right_mouse", 0xca00, 0x47, True),
        TexConfBinding("left_control", 0xe000, 0x00, True),
        TexConfBinding("left_shift", 0xe100, 0x12, True),
        TexConfBinding("left_alt", 0xe200, 0x10, True),
        TexConfBinding("left_win", 0xe300, 0x08, True),
        TexConfBinding("right_control", 0xe400, 0x38, True),
        TexConfBinding("right_shift", 0xe500, 0x31, True),
        TexConfBinding("fn", 0xe600, 0x20, True),
        TexConfBinding("right_alt", 0xe700, 0x28, True),
        TexConfBinding("right_win", 0x6500, 0x30, True),
        TexConfBinding("middle_mouse_click", 0xf201, 0, False),
        TexConfBinding("left_mouse_click", 0xf001, 0, False),
        TexConfBinding("led-", 0x9201, 0, False),
        TexConfBinding("led+", 0x9301, 0, False),
        TexConfBinding("led_on/off", 0x8001, 0, False),
        TexConfBinding("right", 0x4f00, 0, False),
        TexConfBinding("play/pause", 0xf000, 0, False),
        TexConfBinding("prev", 0xf200, 0, False),
        TexConfBinding("next", 0xf300, 0, False),
        TexConfBinding("mute", 0xf400, 0, False),
        TexConfBinding("vol-", 0xf500, 0, False),
        TexConfBinding("vol+", 0xf600, 0, False),
        TexConfBinding("speed+", 0x3a01, 0, False),
        TexConfBinding("speed-", 0x3001, 0, False),
        TexConfBinding("disable", 0xFF00, 0xFF, False),  # When binding to fn layer then should we really disable?
    ]

    def __init__(self):

        super().__init__()

        for profile in TexProfile:
            for layer in TexLayer:
                self.addConfigEntry(profile, layer, "right_win", "right_alt")
                self.addConfigEntry(profile, layer, "right_alt", "fn")

            self.addConfigFnEntry(profile, TexFnLayer.FN_LAYER1, "fn")
            self.addConfigFnEntry(profile, TexFnLayer.FN_LAYER1, "middle_mouse")

        # Keys that does not exist within the default TEX binary file
        # Leaving them here until it can be determined what they are.
        self.unsupportedKeys = [
            0x32,  # Unknown what this key is
            0x35,  # This key is only available if the users has a DIY split backspace key
        ] + list(range(0x3a, 0x65)) + list(range(0x66, 0xc8)) + list(range(0xcb, 0xe0))

        # FN1 default configuration
        prebuiltFnLayer = {
            "a": "left",
            "b": "vol+",
            "c": "next",
            "d": "right",
            "e": "speed+",
            "i": "ins",
            "l": "end",
            "n": "mute",
            "o": "home",
            "p": "pageUp",
            "q": "speed-",
            "s": "down",
            "v": "vol-",
            "w": "up",
            "x": "play/pause",
            "z": "prev",
            "1": "f1",
            "2": "f2",
            "3": "f3",
            "4": "f4",
            "5": "f5",
            "6": "f6",
            "7": "f7",
            "8": "f8",
            "9": "f9",
            "0": "f10",
            "-": "f11",
            "=": "f12",
            "esc": "`",
            "backspace": "del",
            "[": "PrtSc",
            "]": "ScrLk",
            ";": "pageDown",
            "'": "pause",
            ",": "led-",
            ".": "led_on/off",
            "/": "led+"
        }

        # Prepare the default FN1 layer
        for i in range(0, 3):
            for key, value in prebuiltFnLayer.items():
                self.addConfigEntry(TexProfile(i), TexLayer.FN1, key, value)

    def keyIterator(self) -> Generator[int, Any, Any]:
        for i in range(0x04, 0xe8):
            if i not in self.unsupportedKeys:
                yield i
