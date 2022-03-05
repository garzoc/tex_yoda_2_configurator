#!/usr/bin/python3
#no_macro_header = bytearray([0x4359, 0x4649])
#print("hello")

class TexBinaryBuilder:

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

        # Unmappable key
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
    }

    def __init__(self):

        # Keys that does not exist within the default TEX binary file
        # Leaving them here until it can be determined what they are.
        self.unsupportedKeys = [
            0x32, # Unknown what these keys are
            0x35, # Unknown what these keys are
        ] + list(range(0x3a, 0x65)) + list(range(0x66, 0xc8)) + list(range(0xcb, 0xe0))

        self.endOfProfile = bytearray([
            0x02, 0x94 ,0x02, 0x00, 0x20, 0x46 ,0xff ,0xff,
            0x00, 0x00 ,0x00, 0x00 ,0x00, 0x00 ,0x00, 0x00
        ])

        # Currently not known how macros affect the binary file header but it only seems change based
        # on the number of macros so use prebuilt headers for now
        self.no_macro_header = bytearray([
            0x43, 0x59, 0x46, 0x49, 0x00, 0x00, 0x03, 0x00, 0x00, 0x01, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00,
            0x00, 0x02 ,0x00, 0x00, 0x30, 0x08, 0x00, 0x00, 0x00, 0x03 ,0x00, 0x00, 0x40, 0x10, 0x00, 0x00
        ])

        # Define of the naming scheme for every layer of all three profiles
        # and add minor default configuration
        self.configs = {
            "profile1_fn": {},
            "profile1_normal" : {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
            "profile1_third"  : {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
            "profile1_macro"  : {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]}, # Calling Macro for now as it is affected by macro changes
            "profile2_fn": {},
            "profile2_normal" : {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
            "profile2_third"  : {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
            "profile2_macro"  : {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]}, # Calling Macro for now as it is affected by macro changes
            "profile3_fn": {},
            "profile3_normal" : {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
            "profile3_third"  : {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]},
            "profile3_macro"  : {0x6500: [0xe7, 0x00], 0xe700: [0xe6, 0x00]}, # Calling Macro for now as it is affected by macro changes
        }

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

        for i in range(1, 4):
            for key, value in prebuiltFnLayer.items():
                self.addConfigEntry("profile{}_fn".format(i), key, value)

    @staticmethod
    def keyCode(*keys):
        codeList = []
        for key in keys:
            if key in TexBinaryBuilder.keymap:
                codeList.append(TexBinaryBuilder.keymap[key])
            else:
                codeList.append(None)
        return codeList

    def getConfig(self, configName):
        if configName in self.configs:
            return self.configs[configName]
        return {}

    def addConfigEntry(self, name, key, value):
        keyCode, valueCode = TexBinaryBuilder.keyCode(key, value)
        as_bytes = valueCode.to_bytes(2, "big")
        self.configs[name][keyCode] = list(as_bytes)

    def setConfig(self, configs):
        for confName, config in configs.items():                                # Iterate over the list of layer configurations
            if confName in self.configs:                                        # Does the layer exists
                for key, value in config.items():                               # Iterate over keys in the new config
                    if all(x in TexBinaryBuilder.keymap for x in [key, value]): # Is the key mappable
                        self.addConfigEntry(confName, key, value)

    def create_key_mapping(self, key, layer, config, value=None, default=True):
        if value is None:
            value = key

        config_key = (key << 8)
        if(type(config) is dict and config_key in config):
            return bytearray([0x02, 0x20, key, layer] + config[config_key] + [0x00, 0x00])
        elif default:
            # With not config available fallback on default value
            return bytearray([0x02, 0x20, key, layer, value, 0x00, 0x00, 0x00])
        else:
            return None

    def keyIterator(self):
        for i in range(0x04, 0xe8):
            if i not in self.unsupportedKeys:
                yield i

    def binraryGenerate(self, filename, config):

        with open(filename, "wb") as file:
            yield "File header"
            file.write(self.no_macro_header)
            for i in range(1, 4):

                yield
                config = yield "profile{}_fn".format(i)

                for key in self.keyIterator():
                    data = self.create_key_mapping(key, 0x01, config, None, False)
                    if (data):
                        file.write(data)

                yield
                config = yield "Unordered keys"

                # It is not known why in the default configuration the fn_keys are out of order.
                # It would probably be fine to map the keys in any order.
                # This could be removed in the future but keeping it for now to make it easier for testing
                unorderedFnKeys = [
                    "f", "g", "h", "j", "k", "m", "r", "t",
                    "u", "y", "0x2800", "0x2b00", "0x2c00", "\\", "0x3900", "0x6500",
                    "0xc800", "middle_mouse", "0xca00", "0xe000", "0xe100", "0xe200", "0xe300", "0xe400",
                    "0xe500", "0xe600", "0xe700"
                ]

                for key in unorderedFnKeys:
                    # Reconfigured keys are ordered normally
                    if self.keyCode(key)[0] not in config:
                        keyByte = list(self.keyCode(key)[0].to_bytes(2, "big"))[0]
                        if keyByte == 0x65:
                            file.write(self.create_key_mapping(keyByte, 0x01, None, 0xe7))
                        elif keyByte == 0xe7:
                            file.write(self.create_key_mapping(keyByte, 0x01, None, 0xe6))
                        else:
                            file.write(self.create_key_mapping(keyByte, 0x01, None))

                yield
                config = yield "profile{}_normal".format(i)

                for key in self.keyIterator():
                    file.write(self.create_key_mapping(key, 0x02, config))

                yield
                config = yield "profile{}_third".format(i)

                for key in self.keyIterator():
                    file.write(self.create_key_mapping(key, 0x03, config))

                yield
                config = yield "profile{}_macro".format(i)

                for key in self.keyIterator():
                    file.write(self.create_key_mapping(key, 0x00, config))

                yield
                config = yield "profile {} done".format(i)

                file.write(self.endOfProfile)

            # Add remaining bytes to binary file
            for i in range(0, 5080):
                file.write(bytearray([0xFF]))

            yield




def init():
    texBuilder = TexBinaryBuilder()
    #texBuilder.setConfig({"profile1_normal": {"s": "a"}})
    #texBuilder.setConfig({"profile1_fn": {"q": "s"}})
    #texBuilder.setConfig({"profile1_fn": {"f": "s"}})

    generator = texBuilder.binraryGenerate("test.txt", "step")

    #https://stackoverflow.com/questions/22028903/python-generator-send-dont-yield-a-new-value-after-a-send
    for step in generator:
        print("Creating {}".format(step))
        generator.send(texBuilder.getConfig(step))


if __name__ == "__main__":
    init()
