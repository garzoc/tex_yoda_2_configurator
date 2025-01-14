from typing import Generator, Any
from TexConfig import TexProfile, TexLayer, TexFnLayer, TexConfKeyDecl, TexConfigurator


class TexConfiguratorShura(TexConfigurator):
    keyDeclarations = [
        TexConfKeyDecl("a", 0x0400, 0x34, True),  # Untested, but probably fine
        TexConfKeyDecl("b", 0x0500, 0x01, True),
        TexConfKeyDecl("c", 0x0600, 0x32, True),  # Untested, but probably fine
        TexConfKeyDecl("d", 0x0700, 0x03, True),  # Untested, but probably fine
        TexConfKeyDecl("e", 0x0800, 0x15, True),  # Untested, but probably fine
        TexConfKeyDecl("f", 0x0900, 0x0b, True),  # Untested, but probably fine
        TexConfKeyDecl("g", 0x0a00, 0x13, True),  # Untested, but probably fine
        TexConfKeyDecl("h", 0x0b00, 0x1b, True),  # Untested, but probably fine
        TexConfKeyDecl("i", 0x0c00, 0x3d, True),  # Untested, but probably fine
        TexConfKeyDecl("j", 0x0d00, 0x23, True),  # Untested, but probably fine
        TexConfKeyDecl("k", 0x0e00, 0x2b, True),  # Untested, but probably fine
        TexConfKeyDecl("l", 0x0f00, 0x33, True),  # Untested, but probably fine
        TexConfKeyDecl("m", 0x1000, 0x11, True),  # Untested, but probably fine
        TexConfKeyDecl("n", 0x1100, 0x09, True),  # Untested, but probably fine
        TexConfKeyDecl("o", 0x1200, 0x04, True),  # Untested, but probably fine
        TexConfKeyDecl("p", 0x1300, 0x0c, True),  # Untested, but probably fine
        TexConfKeyDecl("q", 0x1400, 0x05, True),  # Untested, but probably fine
        TexConfKeyDecl("r", 0x1500, 0x1d, True),  # Untested, but probably fine
        TexConfKeyDecl("s", 0x1600, 0x3c, True),  # Untested, but probably fine
        TexConfKeyDecl("t", 0x1700, 0x25, True),  # Untested, but probably fine
        TexConfKeyDecl("u", 0x1800, 0x35, True),  # Untested, but probably fine
        TexConfKeyDecl("v", 0x1900, 0x3a, True),  # Untested, but probably fine
        TexConfKeyDecl("w", 0x1a00, 0x0d, True),  # Untested, but probably fine
        TexConfKeyDecl("x", 0x1b00, 0x2a, True),  # Untested, but probably fine
        TexConfKeyDecl("y", 0x1c00, 0x2d, True),  # Untested, but probably fine
        TexConfKeyDecl("z", 0x1d00, 0x22, True),  # Untested, but probably fine
        TexConfKeyDecl("1", 0x1e00, 0x0f, True),  # Untested, but probably fine
        TexConfKeyDecl("2", 0x1f00, 0x17, True),  # Untested, but probably fine
        TexConfKeyDecl("3", 0x2000, 0x1f, True),  # Untested, but probably fine
        TexConfKeyDecl("4", 0x2100, 0x27, True),  # Untested, but probably fine
        TexConfKeyDecl("5", 0x2200, 0x2f, True),  # Untested, but probably fine
        TexConfKeyDecl("6", 0x2300, 0x37, True),  # Untested, but probably fine
        TexConfKeyDecl("7", 0x2400, 0x3f, True),  # Untested, but probably fine
        TexConfKeyDecl("8", 0x2500, 0x06, True),  # Untested, but probably fine
        TexConfKeyDecl("9", 0x2600, 0x0e, True),  # Untested, but probably fine
        TexConfKeyDecl("0", 0x2700, 0x16, True),  # Untested, but probably fine
        TexConfKeyDecl("enter", 0x2800, 0x0a, True),  # Untested, but probably fine
        TexConfKeyDecl("esc", 0x2900, 0x07, True),  # Untested, but probably fine
        TexConfKeyDecl("backspace", 0x2a00, 0x36, True),  # Untested, but probably fine
        TexConfKeyDecl("tab", 0x2b00, 0x3e, True),  # Untested, but probably fine
        TexConfKeyDecl("spacebar", 0x2c00, 0x18, True),  # Untested
        TexConfKeyDecl("-", 0x2d00, 0x1e, True),  # Untested, but probably fine
        TexConfKeyDecl("=", 0x2e00, 0x26, True),  # Untested, but probably fine
        TexConfKeyDecl("[", 0x2f00, 0x14, True),  # Untested, but probably fine
        TexConfKeyDecl("]", 0x3000, 0x1c, True),  # Untested, but probably fine
        TexConfKeyDecl("\\", 0x3100, 0x24, True),  # Untested, but probably fine
        TexConfKeyDecl(";", 0x3300, 0x3b, True),  # Untested, but probably fine
        TexConfKeyDecl("'", 0x3400, 0x02, True),  # Untested, but probably fine
        TexConfKeyDecl("`", 0x3500, 0x2e, False),  # Untested, but probably fin
        TexConfKeyDecl(",", 0x3600, 0x19, True),  # Untested, but probably fine
        TexConfKeyDecl(".", 0x3700, 0x21, True),  # Untested, but probably fine
        TexConfKeyDecl("/", 0x3800, 0x29, True),  # Untested, but probably fine
        TexConfKeyDecl("capslock", 0x3900, 0, False),
        TexConfKeyDecl("f1", 0x3a00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f2", 0x3b00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f3", 0x3c00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f4", 0x3d00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f5", 0x3e00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f6", 0x3f00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f7", 0x4000, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f8", 0x4100, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f9", 0x4200, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f10", 0x4300, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f11", 0x4400, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("f12", 0x4500, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("PrtSc", 0x4600, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("ScrLk", 0x4700, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("pause", 0x4800, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("ins", 0x4900, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("home", 0x4a00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("pageUp", 0x4b00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("del", 0x4c00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("end", 0x4d00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("pageDown", 0x4e00, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("left", 0x5000, 0x41, True),
        TexConfKeyDecl("down", 0x5100, 0x4b, True),  # Untested, but probably fine
        TexConfKeyDecl("up", 0x5200, 0x4c, True),
        TexConfKeyDecl("right", 0x4f00, 0x49, True),
        TexConfKeyDecl("left_mouse", 0xb000, 0, True),  # Can this value be bound to another key?
        TexConfKeyDecl("middle_mouse", 0xb100, 0x46, True),  # Just a best guess since it's not officially remappable
        TexConfKeyDecl("right_mouse", 0xb200, 0, True),
        TexConfKeyDecl("left_control", 0xe000, 0x00, True),  # Untested
        TexConfKeyDecl("left_shift", 0xe100, 0x12, True),  # Untested
        TexConfKeyDecl("left_alt", 0xe200, 0x10, True),  # Untested
        TexConfKeyDecl("left_win", 0xe300, 0x08, True),  # Untested
        TexConfKeyDecl("right_control", 0xe400, 0x38, True),  # Untested
        TexConfKeyDecl("right_shift", 0xe500, 0x31, True),  # Untested
        TexConfKeyDecl("right_alt", 0xe600, 0x30, True),  # Tested
        TexConfKeyDecl("right_win", 0x6500, 0x30, True),  # Untested
        TexConfKeyDecl("middle_mouse_click", 0xf201, 0, False),  # Untested
        TexConfKeyDecl("left_mouse_click", 0xf001, 0, False),  # Untested
        TexConfKeyDecl("play/pause", 0xf000, 0, False),  # Untested
        TexConfKeyDecl("prev", 0xf200, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("next", 0xf300, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("mute", 0xf400, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("vol-", 0xf500, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("vol+", 0xf600, 0, False),  # Untested, but probably fine
        TexConfKeyDecl("speed+", 0x3a01, 0, False),  # Untested
        TexConfKeyDecl("speed-", 0x3001, 0, False),  # Untested
        TexConfKeyDecl("disable", 0xFF00, 0xFF, False),  # When binding to fn layer then should we really disable?
        TexConfKeyDecl("fn", 0xce00, 0x2c, True),

        # This appears to be a unique case for enabling capslock on a key that is has been mapped
        # to fn layer switching
        TexConfKeyDecl("?", 0xe800, 0, False),
    ]

    def __init__(self):

        super().__init__()

        for profile in TexProfile:
            #    self.addConfigEntry(profile, layer, "right_win", "right_alt")
            for layer in TexLayer:
                self.addConfigEntry(profile, layer, 0xce00, 0xe800)

            self.addConfigFnEntry(profile, TexFnLayer.FN_LAYER1, "fn")
            self.addConfigFnEntry(profile, TexFnLayer.FN_LAYER1, "middle_mouse")

        # Keys that does not exist within the default TEX binary file
        # Leaving them here until it can be determined what they are.
        self.unsupportedKeys = [
            0x32,  # Unknown what this key is
            0x35,  # This key is only available if the users has a DIY split backspace key
            0xb1,
        ] + list(range(0x39, 0x4b)) + list(range(0x4c, 0x4e)) + list(range(0x53, 0xb0)) + list(range(
            0xb3, 0xc9)) + list(range(0xca, 0xce)) + list(range(0xcf, 0xe0))

        # FN1 default configuration
        prebuiltFnLayer = {
            "e": "vol+",
            "u": "PrtSc",
            "i": "ins",
            "q": "mute",
            "w": "vol-",
            "up": "pageUp",
            "right": "end",
            "down": "pageDown",
            "left": "home",
            "tab": "capslock",
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
        }

        # Prepare the default FN1 layer
        for i in range(0, 3):
            for key, value in prebuiltFnLayer.items():
                self.addConfigEntry(TexProfile(i), TexLayer.FN1, key, value)

    def keyIterator(self) -> Generator[int, Any, Any]:
        for i in range(0x04, 0xe8):
            if i not in self.unsupportedKeys:
                yield i
