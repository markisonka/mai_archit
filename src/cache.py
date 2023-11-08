class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self._storage = {}

    def get(self, key: str) -> str:
        ret_val = self._storage.get(key)
        if ret_val:
            del self._storage[key]
            self._storage[key] = ret_val
            return ret_val
        return ''

    def set(self, key: str, value: str) -> None:
        if key in self._storage:
            del self._storage[key]
        if len(self._storage) >= self.capacity:
            oldest_key = next(iter(self._storage))
            del self._storage[oldest_key]
        
        self._storage[key] = value

    def rem(self, key: str) -> None:
        del self._storage[key]
