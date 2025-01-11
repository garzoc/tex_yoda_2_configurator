from enum import Enum
from collections import namedtuple
from abc import ABC, abstractmethod
from typing import Generator, Any

TexConfBinding = namedtuple("TexConfBinging", ['name', 'code', 'fn', 'bindable'])


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
    keybindings: list[TexConfBinding] = []
    unsupportedKeys: list[int] = []

    def __init__(self):
        # Define the configuration scheme and include the default configuration
        self.profiles = [
            {
                "layers": {
                    TexLayer.NORMAL: {},
                    TexLayer.FN1:    {},
                    TexLayer.FN2:    {},
                    TexLayer.FN3:    {},
                },
                "fn": {
                    TexFnLayer.FN_LAYER1: [],
                }
            },
            {
                "layers": {
                    TexLayer.NORMAL: {},
                    TexLayer.FN1:    {},
                    TexLayer.FN2:    {},
                    TexLayer.FN3:    {},
                },
                "fn": {
                    TexFnLayer.FN_LAYER1: [],
                }
            },
            {
                "layers": {
                    TexLayer.NORMAL: {},
                    TexLayer.FN1:    {},
                    TexLayer.FN2:    {},
                    TexLayer.FN3:    {},
                },
                "fn": {
                    TexFnLayer.FN_LAYER1: [],
                }
            }
        ]

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

        layer_map[key] = value

    def removeConfigEntry(self, profile: TexProfile, layer: TexLayer, key: str):

        profile_map: dict = self.profiles[profile]
        layer_map = profile_map["layers"].get(layer)

        key_binding = self.getBinding(key)

        """
        Only accept the new config if there is a binding for that key
        """
        if not key_binding or not layer_map.get(key):
            return

        del layer_map[key]

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
            self.removeConfigEntry(profile, layer, key)

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
