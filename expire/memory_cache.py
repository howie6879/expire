#!/usr/bin/env python
import time

from expire.serializer import PickleSerializer
from expire.base_cache import BaseCache


class MemoryCache(BaseCache):
    _cache = {}

    def __init__(self, serializer=None, **kwargs):
        if serializer is None:
            serializer = PickleSerializer
        super().__init__(serializer=serializer, **kwargs)

    def set(self, key, value, ttl=None, **kwargs):
        if ttl:
            ttl = int(time.time()) + int(ttl)
        value = self.serializer.dumps((value, ttl))
        self._cache[key] = value
        return True

    def get(self, key, default=None, **kwargs):
        set_default = self.serializer.dumps((default, None))
        result = self._cache.get(key, set_default)
        result_list = self.serializer.loads(result)
        value = result_list[0]
        if result_list[1] is not None:
            ts = int(time.time())
            if ts > result_list[1]:
                self._delete(key=key)
                value = None
        return value if value is not None else default

    def delete(self, *keys):
        res = []
        for key in keys:
            res.append(self._delete(key))
        return res

    def exists(self, key, **kwargs):
        return key in self._cache

    def incr(self, key, **kwargs):
        result = int(self.get(key, default=0)) + 1
        self.set(key, result)
        return result

    def _delete(self, key):
        return self._cache.pop(key, 0)
