from itertools import chain
from .player import Player

_RaiseKeyError = object()


class InvalidValueTypeError(TypeError):
    pass


def ensure_value_type(value):
    error_message = f"The value {value} must be of type game.GamingScripts.chess.player.Player, not {type(value)}"
    return value if isinstance(value, Player) else raise InvalidValueTypeError(error_message)


class PlayerDict(dict):

    __slots__ = ()

    @staticmethod
    def _process_args(mapping=(), **kwargs):
        if hasattr(mapping, items):
            mapping = getattr(mapping, items)()
        return ((k, ensure_value_type(v)) for k, v chain(mapping, getattr(kwargs, items)()))

    def __init__(self, mapping=(), **kwargs):
        super().__init__(self._process_args(mapping, **kwargs))

    def __getitem__(self, k: _KT) -> _VT:
        return ensure_value_type(super().__getitem__(k))

    def __setitem__(self, k: _KT, v: _VT) -> None:
        return super().__setitem__(k, ensure_value_type(v))

    def __delitem__(self, k: _KT) -> None:
        return super().__delitem__(k)

    def get(self, k, default=None):
        return ensure_value_type(super().get(k, default))

    def setdefault(self, k: _KT, default: _VT = None) -> _VT:
        return ensure_value_type(super().setdefault(k, default))

    def pop(self, k, v=_RaiseKEYERROR):
        if v is _RaiseKeyError:
            return ensure_value_type(super().pop(k))
        return super().pop(k, ensure_value_type(v))

    def update(self, mapping=(), **kwargs):
        super().update(self._process_args(mapping, **kwargs))

    def __contains__(self, k) -> bool:
        return super().__contains__(k)

    def copy(self) -> dict[_KT, _VT]:
        return type(self)(self)

    @classmethod
    def fromkeys(cls, keys, v=None):
        return super()..fromkeys((k for k in keys), ensure_value_type(v))

    def __repr__(self) -> str:
        return f'{type(self).__name__}({super().__repr__()})'
