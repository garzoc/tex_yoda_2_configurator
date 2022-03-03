#!/usr/bin/python3
# Currently not known how macros affect the binary header but it only seems change the number of macros
# so use predefined headers for now
#no_macro_header = bytearray([0x4359, 0x4649])
#print("hello")
no_macro_header = bytearray([0x43, 0x59, 0x46, 0x49, 0x00, 0x00, 0x03, 0x00, 0x00, 0x01, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00,
                             0x00, 0x02 ,0x00, 0x00, 0x30, 0x08, 0x00, 0x00, 0x00, 0x03 ,0x00, 0x00, 0x40, 0x10, 0x00, 0x00])

fn_layer = bytearray([
0x02, 0x20 ,0x04, 0x01 ,0x50, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x05, 0x01 ,0xf6, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x06, 0x01 ,0xf3, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x07, 0x01 ,0x4f, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x08, 0x01 ,0x3a, 0x01 ,0x00, 0x00 ,0x02 ,0x20 ,0x0c, 0x01 ,0x49, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x0f, 0x01 ,0x4d, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x11, 0x01 ,0xf4, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x12, 0x01 ,0x4a, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x13, 0x01 ,0x4b, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x14, 0x01 ,0x30, 0x01 ,0x00, 0x00 ,0x02 ,0x20 ,0x16, 0x01 ,0x51, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x19, 0x01 ,0xf5, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x1a, 0x01 ,0x52, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x1b, 0x01 ,0xf0, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x1d, 0x01 ,0xf2, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x1e, 0x01 ,0x3a, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x1f, 0x01 ,0x3b, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x20, 0x01 ,0x3c, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x21, 0x01 ,0x3d, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x22, 0x01 ,0x3e, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x23, 0x01 ,0x3f, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x24, 0x01 ,0x40, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x25, 0x01 ,0x41, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x26, 0x01 ,0x42, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x27, 0x01 ,0x43, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x29, 0x01 ,0x35, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x2a, 0x01 ,0x4c, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x2d, 0x01 ,0x44, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x2e, 0x01 ,0x45, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x2f, 0x01 ,0x46, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x30, 0x01 ,0x47, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x33, 0x01 ,0x4e, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x34, 0x01 ,0x48, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x36, 0x01 ,0x92, 0x01 ,0x00, 0x00 ,0x02 ,0x20 ,0x37, 0x01 ,0x80, 0x01 ,0x00, 0x00,
0x02, 0x20 ,0x38, 0x01 ,0x93, 0x01 ,0x00, 0x00 ,0x02 ,0x20 ,0x09, 0x01 ,0x09, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x0a, 0x01 ,0x0a, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x0b, 0x01 ,0x0b, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x0d, 0x01 ,0x0d, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x0e, 0x01 ,0x0e, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x10, 0x01 ,0x10, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x15, 0x01 ,0x15, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x17, 0x01 ,0x17, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x18, 0x01 ,0x18, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x1c, 0x01 ,0x1c, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x28, 0x01 ,0x28, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x2b, 0x01 ,0x2b, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x2c, 0x01 ,0x2c, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x31, 0x01 ,0x31, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0x39, 0x01 ,0x39, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0x65, 0x01 ,0xe7, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0xc8, 0x01 ,0xc8, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0xc9, 0x01 ,0xc9, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0xca, 0x01 ,0xca, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0xe0, 0x01 ,0xe0, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0xe1, 0x01 ,0xe1, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0xe2, 0x01 ,0xe2, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0xe3, 0x01 ,0xe3, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0xe4, 0x01 ,0xe4, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0xe5, 0x01 ,0xe5, 0x00 ,0x00, 0x00,
0x02, 0x20 ,0xe6, 0x01 ,0xe6, 0x00 ,0x00, 0x00 ,0x02 ,0x20 ,0xe7, 0x01 ,0xe6, 0x00 ,0x00, 0x00])

keymap = {
    "s": 0x1600,
    "a": 0x0400,
    "q": 0x1400
}

# Keys that does not exists within the default TEX format file
# Leaving them here until it can be determined what they do.
unsupported_keys = [
    0x32, # Unknown what these keys are
    0x35, # Unknown what these keys are
] + list(range(0x3a, 0x65)) + list(range(0x66, 0xc8)) + list(range(0xcb, 0xe0))

def create_key_mapping(key, layer, config):
    config_key = (key << 8) | layer
    if(config_key in config):
        return bytearray([0x02, 0x20, key, layer] + config[config_key] + [0x00, 0x00])
    else:
        # With not config available fallback on default value
        return bytearray([0x02, 0x20, key, layer, key, 0x00, 0x00, 0x00])

def init():
    newFile = open("test.txt", "wb")
    newFile.write(no_macro_header)
    newFile.write(fn_layer)
    for i in range(0x04, 0xe8):
        if i not in unsupported_keys:
            #newFile.write(bytearray([0x02, 0x20, i, 0x02, i, 0x00, 0x00, 0x00]))
            newFile.write(create_key_mapping(i, 0x02, {}))

    for i in range(0x04, 0xe8):
        if i not in unsupported_keys:
            newFile.write(create_key_mapping(i, 0x03, {}))
            #newFile.write(bytearray([0x02, 0x20, i, 0x03, i, 0x00, 0x00, 0x00]))

    for i in range(0x04, 0xe8):
        if i not in unsupported_keys:
            newFile.write(create_key_mapping(i, 0x00, {}))
            #newFile.write(bytearray([0x02, 0x20, i, 0x00, i, 0x00, 0x00, 0x00]))
    newFile.close()



if __name__ == "__main__":
    print("wow")
    init()