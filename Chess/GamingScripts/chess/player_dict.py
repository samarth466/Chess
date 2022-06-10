from itertools import chain
from typing import KeysView, ValuesView
from .player import Player

str_base = str, bytes, bytearray
items = 'items'
print(__package__)

_RaiseKeyError = object()


class InvalidValueTypeError(TypeError):
    pass


class InvalidKeyTypeError(TypeError):
    pass


def ensure_value_type(value):
    error_message = f"The value {value} must be of type game.GamingScripts.chess.player.Player, not {type(value)}"
    if isinstance(value, Player):
        return value
    else:
        raise InvalidValueTypeError(error_message)


def ensure_numerical_key(key):
    if isinstance(key, int):
        return key
    elif isinstance(key, str):
        if key.isnumeric():
            return int(key)
        else:
            raise InvalidKeyTypeError(
                f"The key must be a numeric string, not {key.__class__.__name__}")
    else:
        try:
            return int(key)
        except ValueError as e:
            raise InvalidKeyTypeError(e)


class PlayerDict(dict):

    __slots__ = ()

    @staticmethod
    def _process_args(mapping=(), **kwargs):
        if hasattr(mapping, items):
            mapping = getattr(mapping, items)()
        return ((ensure_numerical_key(k), ensure_value_type(v)) for k, v in chain(mapping, getattr(kwargs, items)()))

    def __init__(self, mapping=(), **kwargs):
        super().__init__(self._process_args(mapping, **kwargs))

    def keys(self) -> KeysView:
        return super().keys()

    def values(self) -> ValuesView:
        return super().values()

    def __getitem__(self, k):
        return super().__getitem__(k)

    def __setitem__(self, k, v) -> None:
        return super().__setitem__(ensure_numerical_key(k), ensure_value_type(v))

    def __delitem__(self, k) -> None:
        return super().__delitem__(k)

    def get(self, k, default=None):
        return super().get(k, default)

    def setdefault(self, k, default=None):
        return ensure_value_type(super().setdefault(ensure_numerical_key(k), default))

    def pop(self, k, v=_RaiseKeyError):
        if v is _RaiseKeyError:
            return ensure_value_type(super().pop(ensure_numerical_key(k)))
        return super().pop(ensure_numerical_key(k), ensure_value_type(v))

    def update(self, mapping=(), **kwargs):
        super().update(self._process_args(mapping, **kwargs))

    def __contains__(self, k) -> bool:
        return super().__contains__(ensure_numerical_key(k))

    def copy(self) -> dict:
        return type(self)(self)

    @classmethod
    def fromkeys(cls, keys, v=None):
        return super().fromkeys((ensure_numerical_key(k) for k in keys), ensure_value_type(v))

    def __repr__(self) -> str:
        return f"{type(self).__name__}({super().__repr__()})"

    def update_current_key(self) -> tuple[Player, int]:
        current_key = list(self.keys())[0]
        while True:
            if current_key == len(self.keys()):
                current_key = self.keys[0]
            yield self[current_key]
            current_key += 1
