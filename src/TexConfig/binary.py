from TexConfig import TexProfile, TexLayer, TexFnLayer, TexConfKeyDecl, TexConfigurator


class TexBinaryBuilder:
    binary_header = bytearray([0x43, 0x59, 0x46, 0x49, 0x00, 0x00])
    ENTRY_SIZE = 8  # Number of bytes for a standard entry
    FN_LAYER_CONFIG_SIZE = 16  # Number of bytes for a FN config entry

    def __init__(self, config: TexConfigurator):
        self.texConfig: TexConfigurator = config  # TexConfigurator

    @property
    def config(self) -> TexConfigurator:
        return self.texConfig

    def getMappedValue(self, key: int, profile: TexProfile, layer: TexLayer, value=None, default=True):
        if value is None:
            value = key

        config_key = (key << 8)
        key_decl: TexConfKeyDecl | None = self.config.getKeyDeclaration(config_key)
        map_to: TexConfKeyDecl | None = self.config.getLayerKeyBinding(profile, layer, key_decl)

        if map_to:
            return bytearray([0x02, 0x20, key, layer] + list(map_to.code.to_bytes(2, "big")) + [0x00, 0x00])

        if default:
            # With not config available fallback on default value
            return bytearray([0x02, 0x20, key, layer, value, 0x00, 0x00, 0x00])

        return None

    def getProfileAddress(self, profile: TexProfile):
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

    def genProfileAndMacroMetaData(self, profile: TexProfile) -> bytearray:
        """
            Write meta data in the header.
            This includes the starting address of each profile.
            As well as the starting address of any configured macros.
            Macros are not configured per profile.
        """
        profile_section_byte_offset = self.getProfileAddress(profile)
        profile_field_key = bytearray([0x00, profile + 1])
        seperator = bytearray([0x00, 0x00])
        return profile_field_key + seperator + bytearray(profile_section_byte_offset.to_bytes(2, "little")) + seperator

    def getFnConf(self, profile: TexProfile) -> bytearray:
        """
            Generate the binary data for configuration of keys that are used to change the current FN layer
        """
        print(f"{profile}: {self.config.getFnLayers(profile)}")
        fn_byte_array = bytearray()
        fn_layer: TexFnLayer = TexFnLayer.FN_LAYER1
        for fn_layer in self.config.getFnLayers(profile):

            used_keys = 0
            key_fn_codes = []

            for key in self.config.getFnMap(profile, fn_layer):
                binding = self.config.getKeyDeclaration(key)
                if binding:
                    used_keys += 1
                    key_fn_codes.append(binding.fn)
                else:
                    print(f"Could not find key: {key}")

            # Max 4 keys can be configured to switch to a specific FN layer
            unused = 4 - used_keys
            start = bytearray([0x02, 0x94 + fn_layer])
            key_count = bytearray([0x00 + used_keys, 0x00])
            keys = bytearray(key_fn_codes)
            padding = bytearray([0xFF] * unused)
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
                file.write(self.genProfileAndMacroMetaData(TexProfile(profile_idx)))

            for profile_idx, _ in enumerate(self.config.profiles):
                for i in range(1, 5):  # Write each layer starting at 1 stopping at 0
                    for key in self.config.keyIterator():
                        data = self.getMappedValue(key, TexProfile(profile_idx), TexLayer(i % 4))
                        if (data):
                            file.write(data)
                """
                After writing all layers, generate the fn layer switcher binding
                """
                file.write(self.getFnConf(TexProfile(profile_idx)))
                # Terminate bytes for the profile
                file.write(bytearray([0x00] * 8))

            file.write(bytearray([0xff] * (317 * 16 + 8)))
