
from typing import Generator, Any
from TexConfig import TexProfile, TexLayer, TexFnLayer, TexConfKeyDecl, TexConfigurator


class TexConfiguratorShinobi(TexConfigurator):
    keyDeclarations = [
        TexConfKeyDecl("a", 0x0400, 0x34, True),  # 00000100: 00110100
        TexConfKeyDecl("b", 0x0500, 0x01, True),  # 00000101: 00000001
        TexConfKeyDecl("c", 0x0600, 0x32, True),  # 00000110: 00110010
        TexConfKeyDecl("d", 0x0700, 0x03, True),  # 00000111: 00000011
        TexConfKeyDecl("e", 0x0800, 0x15, True),  # 00001000: 00010101
        TexConfKeyDecl("f", 0x0900, 0x0b, True),  # 00001001: 00001011
        TexConfKeyDecl("g", 0x0a00, 0x13, True),
        TexConfKeyDecl("h", 0x0b00, 0x1b, True),
        TexConfKeyDecl("i", 0x0c00, 0x3d, True),
        TexConfKeyDecl("j", 0x0d00, 0x23, True),
        TexConfKeyDecl("k", 0x0e00, 0x2b, True),
        TexConfKeyDecl("l", 0x0f00, 0x33, True),
        TexConfKeyDecl("m", 0x1000, 0x11, True),
        TexConfKeyDecl("n", 0x1100, 0x09, True),
        TexConfKeyDecl("o", 0x1200, 0x04, True),
        TexConfKeyDecl("p", 0x1300, 0x0c, True),
        TexConfKeyDecl("q", 0x1400, 0x05, True),
        TexConfKeyDecl("r", 0x1500, 0x1d, True),
        TexConfKeyDecl("s", 0x1600, 0x3c, True),
        TexConfKeyDecl("t", 0x1700, 0x25, True),
        TexConfKeyDecl("u", 0x1800, 0x35, True),
        TexConfKeyDecl("v", 0x1900, 0x3a, True),
        TexConfKeyDecl("w", 0x1a00, 0x0d, True),
        TexConfKeyDecl("x", 0x1b00, 0x2a, True),
        TexConfKeyDecl("y", 0x1c00, 0x2d, True),
        TexConfKeyDecl("z", 0x1d00, 0x22, True),
        TexConfKeyDecl("1", 0x1e00, 0x0f, True),
        TexConfKeyDecl("2", 0x1f00, 0x17, True),
        TexConfKeyDecl("3", 0x2000, 0x1f, True),
        TexConfKeyDecl("4", 0x2100, 0x27, True),
        TexConfKeyDecl("5", 0x2200, 0x2f, True),
        TexConfKeyDecl("6", 0x2300, 0x37, True),
        TexConfKeyDecl("7", 0x2400, 0x3f, True),
        TexConfKeyDecl("8", 0x2500, 0x06, True),
        TexConfKeyDecl("9", 0x2600, 0x0e, True),
        TexConfKeyDecl("0", 0x2700, 0x16, True),
        TexConfKeyDecl("enter", 0x2800, 0x0a, True),
        TexConfKeyDecl("esc", 0x2900, 0x07, True),
        TexConfKeyDecl("backspace", 0x2a00, 0x36, True),
        TexConfKeyDecl("tab", 0x2b00, 0x3e, True),
        TexConfKeyDecl("spacebar", 0x2c00, 0x18, True),
        TexConfKeyDecl("-", 0x2d00, 0x1e, True),
        TexConfKeyDecl("=", 0x2e00, 0x26, True),
        TexConfKeyDecl("[", 0x2f00, 0x14, True),
        TexConfKeyDecl("]", 0x3000, 0x1c, True),
        TexConfKeyDecl("\\", 0x3100, 0x24, True),
        TexConfKeyDecl(";", 0x3300, 0x3b, True),
        TexConfKeyDecl("'", 0x3400, 0x02, True),
        TexConfKeyDecl("`", 0x3500, 0x2e, False),  # Can be enabled in DIY config split backspace
        TexConfKeyDecl(",", 0x3600, 0x19, True),
        TexConfKeyDecl(".", 0x3700, 0x21, True),
        TexConfKeyDecl("/", 0x3800, 0x29, True),
        TexConfKeyDecl("capslock", 0x3900, 0x2c, True),
        TexConfKeyDecl("f1", 0x3a00, 0, False),
        TexConfKeyDecl("f2", 0x3b00, 0, False),
        TexConfKeyDecl("f3", 0x3c00, 0, False),
        TexConfKeyDecl("f4", 0x3d00, 0, False),
        TexConfKeyDecl("f5", 0x3e00, 0, False),
        TexConfKeyDecl("f6", 0x3f00, 0, False),
        TexConfKeyDecl("f7", 0x4000, 0, False),
        TexConfKeyDecl("f8", 0x4100, 0, False),
        TexConfKeyDecl("f9", 0x4200, 0, False),
        TexConfKeyDecl("f10", 0x4300, 0, False),
        TexConfKeyDecl("f11", 0x4400, 0, False),
        TexConfKeyDecl("f12", 0x4500, 0, False),
        TexConfKeyDecl("PrtSc", 0x4600, 0, False),
        TexConfKeyDecl("ScrLk", 0x4700, 0, False),
        TexConfKeyDecl("pause", 0x4800, 0, False),
        TexConfKeyDecl("ins", 0x4900, 0, False),
        TexConfKeyDecl("home", 0x4a00, 0, False),
        TexConfKeyDecl("pageUp", 0x4b00, 0, False),
        TexConfKeyDecl("del", 0x4c00, 0, False),
        TexConfKeyDecl("end", 0x4d00, 0, False),
        TexConfKeyDecl("pageDown", 0x4e00, 0, False),
        TexConfKeyDecl("left", 0x5000, 0, False),
        TexConfKeyDecl("down", 0x5100, 0, False),
        TexConfKeyDecl("up", 0x5200, 0, False),
        TexConfKeyDecl("left_mouse", 0xc800, 0x45, True),  # Can this value be bound to another key?
        TexConfKeyDecl("middle_mouse", 0xc900, 0x46, True),  # Does rebinding change the default scroll behavior?
        TexConfKeyDecl("right_mouse", 0xca00, 0x47, True),
        TexConfKeyDecl("left_control", 0xe000, 0x00, True),
        TexConfKeyDecl("left_shift", 0xe100, 0x12, True),
        TexConfKeyDecl("left_alt", 0xe200, 0x10, True),
        TexConfKeyDecl("left_win", 0xe300, 0x08, True),
        TexConfKeyDecl("right_control", 0xe400, 0x38, True),
        TexConfKeyDecl("right_shift", 0xe500, 0x31, True),
        TexConfKeyDecl("fn", 0xe600, 0x20, True),
        TexConfKeyDecl("right_alt", 0xe700, 0x28, True),
        TexConfKeyDecl("right_win", 0x6500, 0x30, True),
        TexConfKeyDecl("middle_mouse_click", 0xf201, 0, False),
        TexConfKeyDecl("left_mouse_click", 0xf001, 0, False),
        TexConfKeyDecl("led-", 0x9201, 0, False),
        TexConfKeyDecl("led+", 0x9301, 0, False),
        TexConfKeyDecl("led_on/off", 0x8001, 0, False),
        TexConfKeyDecl("right", 0x4f00, 0, False),
        TexConfKeyDecl("play/pause", 0xf000, 0, False),
        TexConfKeyDecl("prev", 0xf200, 0, False),
        TexConfKeyDecl("next", 0xf300, 0, False),
        TexConfKeyDecl("mute", 0xf400, 0, False),
        TexConfKeyDecl("vol-", 0xf500, 0, False),
        TexConfKeyDecl("vol+", 0xf600, 0, False),
        TexConfKeyDecl("speed+", 0x3a01, 0, False),
        TexConfKeyDecl("speed-", 0x3001, 0, False),
        TexConfKeyDecl("disable", 0xFF00, 0xFF, False),  # When binding to fn layer then should we really disable?
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
