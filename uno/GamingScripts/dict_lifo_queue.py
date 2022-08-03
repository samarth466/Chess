from queue import LifoQueue
from typing import _KT, _VT

class DictLifoQueue(LifoQueue):

    def _init(self, maxsize: int) -> None:
        super()._init(maxsize)
        self.queue = {}
    
    def _put(self, item: tuple[_KT,_VT]) -> None:
        self.queue[item[0]] = item[1]
    
    def _get(self) -> _VT:
        return self.queue.pop(list(self.queue.keys())[-1])