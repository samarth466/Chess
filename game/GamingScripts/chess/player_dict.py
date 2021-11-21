from itertools import chain
from .player import Player

_RaiseKeyError = object()


class InvalidValueTypeError(TypeError):
    pass


class InvalidKeyTypeError(TypeError):
    pass


def ensure_value_type(value):
    error_message = f"The value {value} must be of type game.GamingScripts.chess.player.Player, not {type(value)}"
    return value if isinstance(value, Player) else raise InvalidValueTypeError(error_message)


def ensure_numerical_key(key):
    if isinstance(key, int):
        return key
    elif isinstance(key, str):
        if key.isnumeric():
            return int(key)
        else:
            raise InvalidKeyTypeError(
                f"The key must be a numeric string, not {key}")
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
        self.current_key = self.keys()[0]
    
    def keys(self) -> _dict_keys[_KT, _VT]:
        keys_list = super().keys()
        keys = super().keys()
        for index, key in enumerate(keys_list):
            keys[index] = ensure_numerical_key(key)
        return keys
    
    def values(self) -> _dict_values[_VT, _KT]:
        values_list = super().values()
        values = super().values()
        for index, value in enumerate(values_list):
            values[index] = ensure_value_type(value)
        return values
    
    def __getitem__(self, k: _KT) -> _VT:
        return ensure_value_type(super().__getitem__(ensure_numerical_key(k)))

    def __setitem__(self, k: _KT, v: _VT) -> None:
        return super().__setitem__(ensure_numerical_key(k), ensure_value_type(v))

    def __delitem__(self, k: _KT) -> None:
        return super().__delitem__(ensure_numerical_key(k))

    def get(self, k, default=None):
        return ensure_value_type(super().get(ensure_numerical_key(k), default))

    def setdefault(self, k: _KT, default: _VT = None) -> _VT:
        return ensure_value_type(super().setdefault(ensure_numerical_key(k), default))

    def pop(self, k, v=_RaiseKEYERROR):
        if v is _RaiseKeyError:
            return ensure_value_type(super().pop(ensure_numerical_key(k)))
        return super().pop(ensure_numerical_key(k), ensure_value_type(v))

    def update(self, mapping=(), **kwargs):
        super().update(self._process_args(mapping, **kwargs))

    def __contains__(self, k) -> bool:
        return super().__contains__(ensure_numerical_key(k))

    def copy(self) -> dict[_KT, _VT]:
        return type(self)(self)

    @classmethod
    def fromkeys(cls, keys, v=None):
        return super().fromkeys((ensure_numerical_key(k) for k in keys), ensure_value_type(v))

    def __repr__(self) -> str:
        return f"{type(self).__name__}({super().__repr__()})"

    def update_current_key(self) -> tuple[Player,int]:
        if self.current_key == len(self):
            self.current_key = self.keys()[0]
            return self.values()[0], self.keys()[0]
        else:
            self.current_key += 1
            return self[self.current_key], self.current_key