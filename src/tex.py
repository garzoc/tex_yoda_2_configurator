#!/usr/bin/env python3

from enum import Enum
from collections import namedtuple

TexConfBinding = namedtuple("TexConfBinging", ['name', 'code', 'fn', 'bindable'])


# https://stackoverflow.com/questions/58608361/string-based-enum-in-python
class TexLayer(int, Enum):
    NORMAL = 0
    FN1 = 1
    FN2 = 2
    FN3 = 3


class TexFnLayer(int, Enum):
    FN_LAYER1 = 0
    FN_LAYER2 = 1
    FN_LAYER3 = 2


class TexProfile(int, Enum):
    PROFILE_1 = 0
    PROFILE_2 = 1
    PROFILE_3 = 2


class TexConfigurator:
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
        # Define the configuration scheme and include the default configuration
        self.profiles = [
            {
                "layers": {
                    TexLayer.NORMAL: {"right_win": "right_alt", "right_alt": "fn"},
                    TexLayer.FN1:    {"right_win": "right_alt", "right_alt": "fn"},
                    TexLayer.FN2:    {"right_win": "right_alt", "right_alt": "fn"},
                    TexLayer.FN3:    {"right_win": "right_alt", "right_alt": "fn"},
                },
                "fn": {
                    # Default configuration  when enabling the FN1 layer
                    TexFnLayer.FN_LAYER1: ["fn", "middle_mouse"],
                }
            },
            {
                "layers": {
                    TexLayer.NORMAL: {"right_win": "right_alt", "right_alt": "fn"},
                    TexLayer.FN1:    {"right_win": "right_alt", "right_alt": "fn"},
                    TexLayer.FN2:    {"right_win": "right_alt", "right_alt": "fn"},
                    TexLayer.FN3:    {"right_win": "right_alt", "right_alt": "fn"},
                },
                "fn": {
                    # Default configuration  when enabling the FN1 layer
                    TexFnLayer.FN_LAYER1: ["fn", "middle_mouse"],
                }
            },
            {
                "layers": {
                    TexLayer.NORMAL: {"right_win": "right_alt", "right_alt": "fn"},
                    TexLayer.FN1:    {"right_win": "right_alt", "right_alt": "fn"},
                    TexLayer.FN2:    {"right_win": "right_alt", "right_alt": "fn"},
                    TexLayer.FN3:    {"right_win": "right_alt", "right_alt": "fn"},
                },
                "fn": {
                    # Default configuration  when enabling the FN1 layer
                    TexFnLayer.FN_LAYER1: ["fn", "middle_mouse"],
                }
            }
        ]

        # Keys that does not exist within the default TEX binary file
        # Leaving them here until it can be determined what they are.
        self.unsupportedKeys = [
            0x32,  # Unknown what this key is
            0x35,  # This key is only available if the users has a DIY split backspace key
        ] + list(range(0x3a, 0x65)) + list(range(0x66, 0xc8)) + list(range(0xcb, 0xe0))

        # self.binary_header = bytearray([0x43, 0x59, 0x46, 0x49, 0x00, 0x00])

        # Fn1 defalut configuration
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

    def getBindings(self, *keys: str | int) -> list[TexConfBinding | None]:
        result = list(filter(lambda x: x.name in keys or x.code in keys, self.keybindings))
        assert len(keys) >= len(result), f"Duplicate entires in key map, keys searched: {keys}"
        return result + [None] * (len(keys) - len(result))

    def getBinding(self, key: str | int) -> TexConfBinding | None:
        if not key:
            return None
        result = self.getBindings(key)
        return result[0]

    def addConfigEntry(self, profile: TexProfile, layer: TexLayer, key: str, value: str):
        for fn_layer in TexFnLayer:
            self.removeConfigFnEntry(profile, fn_layer, key)

        profile_map: dict = self.profiles[profile]
        layer_map = profile_map["layers"].get(layer)

        key_binding, value_binding = self.getBindings(key, value)

        """
        Only accept the new config if there is a binding for that key & value
        """
        if not key_binding or not value_binding:
            return

        # self.isKeyMapped(profile, key_binding)
        layer_map[key] = value

    def isKeyMapped(self, profile: TexProfile, key_binding: TexConfBinding):
        profile_map = self.profiles[profile]

        for layer in profile_map["layers"]:
            if key_binding.name in profile_map["layers"][layer]:
                print(f"Found existing binding for {key_binding.name}")

        for fn_layer in profile_map["fn"]:
            if key_binding.name in profile_map["layers"][fn_layer]:
                print(f"Found existing binding for {key_binding.name}")

    def removeConfigFnEntry(self, profile: TexProfile, fn_layer: TexFnLayer, key: str):
        profile_map: dict = self.profiles[profile]
        key_binding = self.getBinding(key)

        """
        Only accept the new config if there is a binding for that key & value
        """
        if not key_binding:
            return

        fn_layer_map = profile_map["fn"].get(fn_layer, [])
        fn_layer_map = list(filter(lambda x: x != key, fn_layer_map))

        if len(fn_layer_map) > 0:
            profile_map["fn"][fn_layer] = fn_layer_map
        elif profile_map["fn"].get(fn_layer):
            del profile_map["fn"][fn_layer]

    def addConfigFnEntry(self, profile: TexProfile, fn_layer: TexFnLayer, key: str):
        for layer in TexLayer:
            self.addConfigEntry(profile, layer, key, "disable")

        profile_map: dict = self.profiles[profile]

        key_binding = self.getBinding(key)

        """
        Only accept the new config if there is a binding for that key & value
        """
        if not key_binding or not key_binding.bindable:
            return

        fn_layer_map = profile_map["fn"].get(fn_layer, [])
        fn_layer_map.append(key)
        profile_map["fn"][fn_layer] = fn_layer_map

    def keyIterator(self):
        for i in range(0x04, 0xe8):
            if i not in self.unsupportedKeys:
                yield i

    def profileLen(self):
        return len([i for i in list(range(0x04, 0xe8)) if i not in self.unsupportedKeys])

    def layerCount(self, profile: TexProfile):
        return len(self.profiles[profile]["layers"])

    def fnCount(self, profile: TexProfile):
        """
        Get the current number of enabled fn layers.
        """
        return len(self.profiles[profile]["fn"])


class TexBinaryBuilder:
    binary_header = bytearray([0x43, 0x59, 0x46, 0x49, 0x00, 0x00])
    ENTRY_SIZE = 8  # Number of bytes for a standard entry
    FN_LAYER_CONFIG_SIZE = 16  # Number of bytes for a FN config entry

    def __init__(self, config: TexConfigurator):
        self.texConfig: TexConfigurator = config  # TexConfigurator

    @property
    def config(self) -> TexConfigurator:
        return self.texConfig

    def get_mapped_value(self, key: int, profile: TexProfile, layer_idx: int, value=None, default=True):
        if value is None:
            value = key
        profile_map: dict = self.config.profiles[profile]
        layer_map = profile_map["layers"][TexLayer(layer_idx)]

        config_key = (key << 8)
        binding: TexConfBinding | None = self.config.getBinding(config_key)

        if binding:
            remap_target: str = layer_map.get(binding.name)
            target_binding: TexConfBinding | None = self.config.getBinding(remap_target)

            if target_binding:
                return bytearray([0x02, 0x20, key, layer_idx] + list(target_binding.code.to_bytes(2, "big")) +
                                 [0x00, 0x00])
        if default:
            # With not config available fallback on default value
            return bytearray([0x02, 0x20, key, layer_idx, value, 0x00, 0x00, 0x00])

        return None

    def get_profile_address(self, profile: TexProfile):
        """
        Find the current starting address of profile 1,2 or 3, by summing the size of all headers
        and content of previous profiles.
        """
        header = len(TexBinaryBuilder.binary_header) + 2
        profiles = TexBinaryBuilder.ENTRY_SIZE * len(self.config.profiles)
        macros = TexBinaryBuilder.ENTRY_SIZE * 0  # This would be the number of macros that we have
        length = header + profiles + macros
        for i in range(0, profile):
            length += (self.config.profileLen() * self.config.layerCount(TexProfile(i)) *
                       TexBinaryBuilder.ENTRY_SIZE)

            """ The lenght of each fn layer will always be the same regardles of the number of bindings
            so all that we have to do is to count the number of enabled layers. """
            length += self.config.fnCount(profile) * TexBinaryBuilder.FN_LAYER_CONFIG_SIZE

        return length

    def gen_profile_and_macro_meta_data(self, profile: TexProfile) -> bytearray:
        """
            Write meta data in the header.
            This includes the starting address of each profile.
            As well as the starting address of any configured macros.
            Macros are not configured per profile.
        """
        profile_section_byte_offset = self.get_profile_address(profile)
        print(f"Offset is {profile_section_byte_offset}")
        profile_field_key = bytearray([0x00, profile + 1])
        seperator = bytearray([0x00, 0x00])
        return profile_field_key + seperator + bytearray(profile_section_byte_offset.to_bytes(2, "little")) + seperator

    def getFnConf(self, profile_idx: TexProfile) -> bytearray:
        """
            Generate the binary data for configuration of keys that are used to change the current FN layer
        """
        profile_map: dict = self.config.profiles[profile_idx]
        fn_map = profile_map["fn"]
        print(fn_map)
        fn_byte_array = bytearray()
        for fn_layer in fn_map:

            used_keys = 0
            key_fn_codes = []

            for key in fn_map[fn_layer]:
                binding = self.config.getBinding(key)
                if binding:
                    used_keys += 1
                    key_fn_codes.append(binding.fn)
                else:
                    print(f"Could not find binding for {key}")

            # Max 4 keys can be configured to switch to a specific FN layer
            unsued = 4 - used_keys
            start = bytearray([0x02, 0x94 + fn_layer])
            key_count = bytearray([0x00 + used_keys, 0x00])
            keys = bytearray(key_fn_codes)
            padding = bytearray([0xFF] * unsued)
            fn_byte_array += start + key_count + keys + padding
        return fn_byte_array

    def writeHeadMetaDataEntriesCount(self):
        """
        This stores the number of meta data fields that is present in the header section.
        Fields that can be found here is the profile section starting address as well as the starting address
        of any macro present in the footer.

        Profile Data
        0001 0000 3800 0000

        Macro data
        0101 0000 6818 0000

        There is currently no support for macros, and we'll always assume that there are always three profiles.

        It might be that this counter is just stored in little endian
        """

        number_of_profiles: int = 0x03
        return bytearray([number_of_profiles, 0x00])

    def binaryGenerate(self, filename):

        with open(filename, "wb") as file:
            file.write(self.binary_header)

            file.write(self.writeHeadMetaDataEntriesCount())

            for profile_idx, _ in enumerate(self.config.profiles):
                file.write(self.gen_profile_and_macro_meta_data(TexProfile(profile_idx)))

            for profile_idx, _ in enumerate(self.config.profiles):
                for i in range(1, 5):  # Write each layer starting at 1 stopping at 0
                    print(i % 4)
                    for key in self.config.keyIterator():
                        data = self.get_mapped_value(key, TexProfile(profile_idx), i % 4)
                        if (data):
                            file.write(data)
                """
                After writing all layers, generate the fn layer switcher binding
                """
                file.write(self.getFnConf(TexProfile(profile_idx)))
                # Terminate bytes for the profile
                file.write(bytearray([0x00] * 8))

            file.write(bytearray([0xff] * (317 * 16 + 8)))


def init():
    texConfiguration = TexConfigurator()
    # texConfiguration.addConfigEntry(TexProfile.PROFILE_1, TexLayer.NORMAL, "b", "vol-")
    texConfiguration.addConfigFnEntry(TexProfile.PROFILE_1, TexFnLayer.FN_LAYER2, "b")
    texBuilder = TexBinaryBuilder(texConfiguration)

    texBuilder.binaryGenerate("KEYMAP.TEX")


if __name__ == "__main__":
    init()
