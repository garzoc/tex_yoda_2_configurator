#!/usr/bin/env python3

from TexConfig import TexProfile, TexLayer, TexFnLayer, TexConfBinding, TexConfigurator
from TexConfig.yoda2 import TexConfiguratorYoda2
from TexConfig.shura import TexConfiguratorShura
from TexConfig.shinobi import TexConfiguratorShinobi


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
        fn_layer: TexFnLayer = TexFnLayer.FN_LAYER1
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
    yoda2: TexConfigurator = TexConfiguratorYoda2()
    shura: TexConfigurator = TexConfiguratorShura()
    shinobi: TexConfigurator = TexConfiguratorShinobi()

    # yoda2.addConfigEntry(TexProfile.PROFILE_1, TexLayer.NORMAL, "b", "vol-")
    shura.addConfigEntry(TexProfile.PROFILE_1, TexLayer.NORMAL, "b", "vol-")
    shinobi.addConfigEntry(TexProfile.PROFILE_1, TexLayer.NORMAL, "b", "vol-")
    # texConfiguration.addConfigFnEntry(TexProfile.PROFILE_1, TexFnLayer.FN_LAYER2, "b")

    texBuilder = TexBinaryBuilder(yoda2)
    texBuilder.binaryGenerate("KEYMAP.TEX")


if __name__ == "__main__":
    init()
