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

    def change_turn(self, current_player_id: int):
        if current_player_id == len(self):
            return self[1], 1
        else:
            return self[current_player_id+1], current_player_id+1
