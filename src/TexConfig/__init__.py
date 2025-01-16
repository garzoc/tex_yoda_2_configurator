from enum import Enum
from collections import namedtuple
from abc import ABC, abstractmethod
from typing import Generator, Any

TexConfKeyDecl = namedtuple("TexConfKeyDecl", ['name', 'code', 'fn', 'bindable'])


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


class TexConfigurator(ABC):
    keyDeclarations: list[TexConfKeyDecl] = []
    unsupportedKeys: list[int] = []

    def __init__(self):
        # Define the configuration scheme and include the default configuration
        self.profiles = [{
            "layers": {
                TexLayer.NORMAL: {},
                TexLayer.FN1: {},
                TexLayer.FN2: {},
                TexLayer.FN3: {},
            },
            "fn": {
                TexFnLayer.FN_LAYER1: [],
            }
        }, {
            "layers": {
                TexLayer.NORMAL: {},
                TexLayer.FN1: {},
                TexLayer.FN2: {},
                TexLayer.FN3: {},
            },
            "fn": {
                TexFnLayer.FN_LAYER1: [],
            }
        }, {
            "layers": {
                TexLayer.NORMAL: {},
                TexLayer.FN1: {},
                TexLayer.FN2: {},
                TexLayer.FN3: {},
            },
            "fn": {
                TexFnLayer.FN_LAYER1: [],
            }
        }]

    def getProfileMap(self, profile: TexProfile):
        return self.profiles[profile]

    def getLayerMap(self, profile: TexProfile, layer: TexLayer) -> dict[str | int, str | int]:
        return self.getProfileMap(profile)["layers"][layer]

    def getFnLayers(self, profile: TexProfile) -> dict[TexFnLayer, list[str | int]]:
        return self.getProfileMap(profile)["fn"]

    def getFnMap(self, profile: TexProfile, fn_layer: TexFnLayer) -> list[str | int]:
        return self.getProfileMap(profile)["fn"][fn_layer]

    def getKeyDeclarations(self, *keys: str | int) -> list[TexConfKeyDecl | None]:
        result = list(filter(lambda x: x.name in keys or x.code in keys, self.keyDeclarations))
        assert len(keys) >= len(result), f"Duplicate entires in key map, keys searched: {keys}"
        return result + [None] * (len(keys) - len(result))

    def getKeyDeclaration(self, key: str | int | None) -> TexConfKeyDecl | None:
        if not key:
            return None
        result = self.getKeyDeclarations(key)
        return result[0]

    def addConfigEntry(self, profile: TexProfile, layer: TexLayer, key: str | int, value: str | int):
        for fn_layer in TexFnLayer:
            self.removeConfigFnEntry(profile, fn_layer, key)

        profile_map: dict = self.profiles[profile]
        layer_map = profile_map["layers"].get(layer)

        key_binding, value_binding = self.getKeyDeclarations(key, value)

        """
        Only accept the new config if there is a binding for that key & value
        """
        if not key_binding or not value_binding:
            return

        layer_map[key] = value

    def removeConfigEntry(self, profile: TexProfile, layer: TexLayer, key: str):

        profile_map: dict = self.profiles[profile]
        layer_map = profile_map["layers"].get(layer)

        key_binding = self.getKeyDeclaration(key)

        """
        Only accept the new config if there is a binding for that key
        """
        if not key_binding or (not layer_map.get(key) and not layer_map.get(key_binding.code)):
            return

        key = layer_map.get(key) or key_binding.code

        del layer_map[key]

    def isKeyMapped(self, profile: TexProfile, key_binding: TexConfKeyDecl):
        profile_map = self.profiles[profile]

        for layer in profile_map["layers"]:
            if key_binding.name in profile_map["layers"][layer]:
                print(f"Found existing binding for {key_binding.name}")

        for fn_layer in profile_map["fn"]:
            if key_binding.name in profile_map["layers"][fn_layer]:
                print(f"Found existing binding for {key_binding.name}")

    def removeConfigFnEntry(self, profile: TexProfile, fn_layer: TexFnLayer, key: str | int):
        profile_map: dict = self.profiles[profile]
        key_binding = self.getKeyDeclaration(key)

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
            self.removeConfigEntry(profile, layer, key)

        for fn_layer_iter in TexFnLayer:
            self.removeConfigFnEntry(profile, fn_layer_iter, key)

        profile_map: dict = self.profiles[profile]

        key_decl = self.getKeyDeclaration(key)

        """
        Only accept the new config if there is a binding for that key & value
        """
        if not key_decl or not key_decl.bindable:
            print(f"Could not bind {key_decl}")
            return

        fn_layer_map = profile_map["fn"].get(fn_layer, [])
        fn_layer_map.append(key)
        profile_map["fn"][fn_layer] = fn_layer_map

    """
    Find from the key binding return the value binding it is supposed to be mapped to according
    to the current configuration.
    """
    def getLayerKeyBinding(self, profile: TexProfile, layer: TexLayer,
                           key: TexConfKeyDecl | None) -> TexConfKeyDecl | None:

        if not key:
            return key

        layer_map = self.getLayerMap(profile, layer)
        target_str: str | int | None = layer_map.get(key.name) or layer_map.get(key.code)
        target_binding: TexConfKeyDecl | None = self.getKeyDeclaration(target_str)

        return target_binding

    @abstractmethod
    def keyIterator(self) -> Generator[int, Any, Any]:
        pass

    def profileLen(self):
        return len([i for i in self.keyIterator()])

    def layerCount(self, profile: TexProfile):
        return len(self.profiles[profile]["layers"])

    def fnCount(self, profile: TexProfile):
        """
        Get the current number of enabled fn layers.
        """
        return len(self.profiles[profile]["fn"])
