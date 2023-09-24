#!/usr/bin/python3

from enum import Enum


# https://stackoverflow.com/questions/58608361/string-based-enum-in-python
class TexConf(int, Enum):
    NORMAL = 0
    FN1  = 1
    FN2 = 2
    FN3 = 3
    FN_LAYER1 = 4
    FN_LAYER2 = 5
    FN_LAYER3 = 6

class TexConfigurator:
    keymap = {
        "[": 0x2f00,
        "\\": 0x3100,
        "]": 0x3000,
        "a": 0x0400,
        "b": 0x0500,
        "c": 0x0600,
        "d": 0x0700,
        "e": 0x0800,
        "f": 0x0900,
        "g": 0x0a00,
        "h": 0x0b00,
        "i": 0x0c00,
        "j": 0x0d00,
        "k": 0x0e00,
        "l": 0x0f00,
        "m": 0x1000,
        "n": 0x1100,
        "o": 0x1200,
        "p": 0x1300,
        "q": 0x1400,
        "r": 0x1500,
        "s": 0x1600,
        "t": 0x1700,
        "u": 0x1800,
        "v": 0x1900,
        "w": 0x1a00,
        "x": 0x1b00,
        "y": 0x1c00,
        "z": 0x1d00,
        "-": 0x2d00,
        "=": 0x2e00,

        # Numbers
        "1": 0x1e00,
        "2": 0x1f00,
        "3": 0x2000,
        "4": 0x2100,
        "5": 0x2200,
        "6": 0x2300,
        "7": 0x2400,
        "8": 0x2500,
        "9": 0x2600,
        "0": 0x2700,

        # TEX YODA, keys that doesn't exist for the default setup Unmappable key
        # Keys that can only be applied as a value

        "f1": 0x3a00,
        "f2": 0x3b00,
        "f3": 0x3c00,
        "f4": 0x3d00,
        "f5": 0x3e00,
        "f6": 0x3f00,
        "f7": 0x4000,
        "f8": 0x4100,
        "f9": 0x4200,
        "f10": 0x4300,
        "f11": 0x4400,
        "f12": 0x4500,

        # Navigation
        "left": 0x5000,
        "right": 0x4f00,
        "down": 0x5100,
        "up": 0x5200,
        "end": 0x4d00,
        "home": 0x4a00,
        "pageUp": 0x4b00,

        # Media
        "play/pause": 0xf000,
        "prev": 0xf200,
        "next": 0xf300,
        "vol+": 0xf600,
        "vol-": 0xf500,
        "mute": 0xf400,

        "speed+": 0x3a01,
        "speed-": 0x3001,
        "ins": 0x4900,

        "middle_mouse": 0xc900,

        "disable": 0xFF00,

        "0x2900": 0x2900,
        "0x3300": 0x3300,
        "0x3600": 0x3600,
        "0x3800": 0x3800,
        "0x2b00": 0x2b00,
        "0x6500": 0x6500,
        "0xe000": 0xe000,
        "0xe200": 0xe200,
        "0xe400": 0xe400,
        "0xe600": 0xe600,

        "0x2a00": 0x2a00,
        "0x3400": 0x3400,
        "0x3700": 0x3700,
        "0x2800": 0x2800,
        "0x2c00": 0x2c00,
        "0x3900": 0x3900,
        "0xc800": 0xc800,
        "0xca00": 0xca00,
        "0xe100": 0xe100,
        "0xe300": 0xe300,
        "0xe500": 0xe500,
        "0xe700": 0xe700,

        "0x3500": 0x3500,
        "0x4600": 0x4600,
        "0x4e00": 0x4e00,
        "0x9201": 0x9201,
        "0x9301": 0x9301,
        "0x2b00": 0x2b00,
        "0xe700": 0xe700,
        "0xe000": 0xe000,
        "0xe200": 0xe200,
        "0xe400": 0xe400,
        "0xe600": 0xe600,

        "0x4c00": 0x4c00,
        "0x4700": 0x4700,
        "0x4800": 0x4800,
        "0x8001": 0x8001,
        "0x2800": 0x2800,
        "0x2c00": 0x2c00,
        "0x3900": 0x3900,
        "0xc800": 0xc800,
        "0xca00": 0xca00,
        "0xe100": 0xe100,
        "0xe300": 0xe300,
        "0xe500": 0xe500,
        "0xe600": 0xe600,

        # Specialized keybindings only for binding FN layer switcher to keys
        "FN_q": 0x05,
        "FN_w": 0x0d,
        "FN_fn": 0x20,           # ??
        "FN_middle_mouse": 0x46,  # ??
    }

    def __init__(self):
        # Define the configuration scheme and include the default configuration
        self.profiles = [
            {
                "layers": {
                    TexConf.NORMAL: {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
                    TexConf.FN1:    {0x6500: [0xe7, 0x00], 0x0400: [0x50, 0x00], 0xe700: [0xe6, 0x00]},
                    TexConf.FN2:    {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
                    TexConf.FN3:    {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
                },
                "fn": {
                    # Default configuration  when enabling the FN1 layer
                    TexConf.FN_LAYER1: ["FN_fn", "FN_middle_mouse"],
                }
            },
            {
                "layers": {
                    TexConf.NORMAL: {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
                    TexConf.FN1:    {0x6500: [0xe7, 0x00], 0x0400: [0x50, 0x00], 0xe700: [0xe6, 0x00]},
                    TexConf.FN2:    {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
                    TexConf.FN3:    {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
                },
                "fn": {
                    # Default configuration  when enabling the FN1 layer
                    TexConf.FN_LAYER1: ["FN_fn", "FN_middle_mouse"],
                }
            },
            {
                "layers": {
                    TexConf.NORMAL: {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
                    TexConf.FN1:    {0x6500: [0xe7, 0x00], 0x0400: [0x50, 0x00], 0xe700: [0xe6, 0x00]},
                    TexConf.FN2:    {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
                    TexConf.FN3:    {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
                },
                "fn": {
                    # Default configuration  when enabling the FN1 layer
                    TexConf.FN_LAYER1: ["FN_fn", "FN_middle_mouse"],
                }
            }
        ]
        # Keys that does not exist within the default TEX binary file
        # Leaving them here until it can be determined what they are.
        self.unsupportedKeys = [
            0x32, # Unknown what these keys are
            0x35, # Unknown what these keys are
        ] + list(range(0x3a, 0x65)) + list(range(0x66, 0xc8)) + list(range(0xcb, 0xe0))

        #self.binary_header = bytearray([0x43, 0x59, 0x46, 0x49, 0x00, 0x00])


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
            "0x2900": "0x3500",
            "0x2a00": "0x4c00",
            "[": "0x4600",
            "]": "0x4700",
            "0x3300": "0x4e00",
            "0x3400": "0x4800",
            "0x3600": "0x9201",
            "0x3700": "0x8001",
            "0x3800": "0x9301"
        }

        # Prepare the default FN1 layer
        for i in range(0, 3):
            for key, value in prebuiltFnLayer.items():
                self.addConfigEntry(i, TexConf.FN1, key, value)

    def getProfileSection(self, profile, section):
        return self.profiles[profile].get(section) or {}

    @staticmethod
    def keyCode(*keys):
        getKey = lambda *keys : (TexConfigurator.keymap[key] if key in TexConfigurator.keymap else None for key in [*keys])
        return getKey(*keys)


    def addConfigEntry(self, profile, section, key, value):
        keyCode, valueCode = TexConfigurator.keyCode(key, value)
        if not all([keyCode, value]):
            print(f"Adding entry for {key} failed")
        as_bytes = valueCode.to_bytes(2, "big")
        self.profiles[profile].get("layers").get(section)[keyCode] = list(as_bytes)

    @staticmethod
    def keyIsConfigurable(key):
        return key in TexConfigurator.keymap

    def keyIterator(self):
        for i in range(0x04, 0xe8):
            if i not in self.unsupportedKeys:
                yield i

    def profileLen(self):
        return len([i for i in list(range(0x04, 0xe8)) if i not in self.unsupportedKeys])

    def layerCount(self, profile):
        return len(self.profiles[profile]["layers"])

    def fnCount(self, profile):
        return len(self.profiles[profile]["fn"])

class TexBinaryBuilder:
    binary_header        = bytearray([0x43, 0x59, 0x46, 0x49, 0x00, 0x00])
    ENTRY_SIZE           = 8 # Number of bytes for a standard entry
    FN_LAYER_CONFIG_SIZE = 16 # Number of bytes for a FN config entry

    def __init__(self, config):
        self.texConfig: TexConfigurator = config  # TexConfigurator

    def getConfig(self, name):
        return self.texConfig.get(name) or {}

    def applyConfig(self, config):
        for index, profile in enumerate(config):                                     # Iterate over the list of layer configurations
            for sectionName, section in profile.layers.items():                                                  # Go through each seaction
                if all([TexConfigurator.keyIsConfigurable(key) for key in section]): # Can the keys be mapped to?
                    # Iterate over keys in the new config
                    for key, value in section.items():
                        self.texConfig.addConfigEntry(index, sectionName, key, value)

    def create_key_mapping(self, key, profile_idx: int, layer_idx: int, value=None, default=True):
        if value is None:
            value = key
        profile: dict = self.texConfig.profiles[profile_idx]
        profile_layer = profile["layers"][TexConf(layer_idx)]
        config_key = (key << 8)
        if(type(profile_layer) is dict and config_key in profile_layer):
            return bytearray([0x02, 0x20, key, layer_idx] + profile_layer[config_key] + [0x00, 0x00])
        elif default:
            # With not config available fallback on default value
            return bytearray([0x02, 0x20, key, layer_idx, value, 0x00, 0x00, 0x00])
        else:
            return None

    def getHeaderData(self, config={}):
        yield [0x20, 0x00]

        # Very hacky expects that there is always an FN layer active
        count = (len(self.getConfig("profile1_fn_layer")) - 1) * 8
        yield [0x30 + count, 0x08]

        # Very hacky expects that there is always an FN layer active
        # This is applies both for profile 1 and 2
        count += (len(self.getConfig("profile2_fn_layer")) - 1) * 8
        yield [0x40, 0x10]

    def getProfileAddress(self, profile):
        header = len(TexBinaryBuilder.binary_header) + 2
        profiles = TexBinaryBuilder.ENTRY_SIZE * len(self.texConfig.profiles)
        macros = TexBinaryBuilder.ENTRY_SIZE * 0
        length = header + profiles + macros
        for i in range(0, profile):
            length += (self.texConfig.profileLen() * self.texConfig.layerCount(profile) * TexBinaryBuilder.ENTRY_SIZE)
            length += self.texConfig.fnCount(profile) * TexBinaryBuilder.FN_LAYER_CONFIG_SIZE

        return length

    def writeProfileHeaderMetaDataField(self, profile_idx) -> bytearray:
        profile_section_byte_offset = self.getProfileAddress(profile_idx - 1)
        profile_field_key = bytearray([0x00, profile_idx])
        seperator = bytearray([0x00, 0x00])
        return profile_field_key + seperator + bytearray(profile_section_byte_offset.to_bytes(2, "little")) + seperator

    def writeFNLayerSwitchInformation(self, profile_idx) -> bytearray:
        profile: dict = self.texConfig.profiles[profile_idx]
        fn_conf = profile["fn"]
        print(fn_conf)
        fn_byte_array = bytearray()
        for i, fn_layer in enumerate(fn_conf.values()):
            print(fn_layer)
            used_keys = len(fn_layer)

            # Max 4 keys can be configured to switch to a specific FN layer
            unsued = 4 - used_keys

            start = bytearray([0x02, 0x94 + i])
            key_count = bytearray([0x00 + used_keys, 0x00])
            keys = bytearray([self.texConfig.keymap[x] for x in fn_layer])
            padding = bytearray([0xFF] * unsued)
            end = bytearray([0x00] * 8)
            fn_byte_array += start + key_count + keys + padding + end
        return fn_byte_array

    def writeHeadMetaDataEntriesCount(self):
        """
        This stores the number of meta data fields that is present in the header section.
        Fields that can be found here is the profile sectation starting address as well as the starting adress
        of any macro present in the footer.

        Profile Data
        0001 0000 3800 0000

        Macro data
        0101 0000 6818 0000

        There is currently no support for macros, and we'll always assume that there are thee profiles.

        It might be that this counter is just stored in little endian
        """

        number_of_profiles: int = 0x03
        return bytearray([number_of_profiles, 0x00])

    def binaryGenerate(self, filename):

        with open(filename, "wb") as file:
            file.write(TexBinaryBuilder.binary_header)

            file.write(self.writeHeadMetaDataEntriesCount())

            for index, profile in enumerate(self.texConfig.profiles):
                length = self.getProfileAddress(index)
                print(f"Hej {hex(length)}")
                file.write(self.writeProfileHeaderMetaDataField(index + 1))

            for profile_idx, profile in enumerate(self.texConfig.profiles):
                for i in range(1, 5):
                    print(i % 4)
                    for key in self.texConfig.keyIterator():
                        data = self.create_key_mapping(key, profile_idx, i % 4)
                        if (data):
                            file.write(data)
                file.write(self.writeFNLayerSwitchInformation(profile_idx))

            for conf in [x for x in TexConf if "fn_layer"]:
                print(conf)
            file.write(bytearray([0xff] * (317 * 16 + 4)))


def init():
    texConfiguration = TexConfigurator()
    texBuilder = TexBinaryBuilder(texConfiguration)
    #texBuilder.setConfig({"profile1_normal": {"s": "a"}})
    #texBuilder.setConfig({"profile1_fn": {"q": "s"}})
    #texBuilder.setConfig({"profile1_fn": {"f": "s"}})

    texBuilder.binaryGenerate("test.txt")

if __name__ == "__main__":
    init()
