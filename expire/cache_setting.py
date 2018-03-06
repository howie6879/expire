#!/usr/bin/env python


from expire.memory_cache import MemoryCache



class CacheSetting:
    """
    Cache setting configuration
    cache_dict provides the basic configuration of the cache
        - cache_class: such as MemoryCache RedisCache etc.
        - cache_config: basic configuration, just like redis's host port db password etc.
        - serializer: such as JsonSerializer PickleSerializer.
    """
    cache_dict = {
        'cache_class': MemoryCache,
        'cache_config': {},
        'serializer': None
    }

    def __init__(self, settings=None):
        self.cache = getattr(settings, 'cache', self.cache_dict)
        if not isinstance(self.cache.get('cache_config'), dict):
            raise ValueError("Key cache_config must be a dict")
        serializer = self.cache.get('serializer')
        self.ttl = self.cache.get('ttl')
        self.instance = self.cache['cache_class'](serializer=serializer, **self.cache['cache_config'])

    def set(self, key, value, ttl=None, **kwargs):
        ttl = ttl or self.ttl
        return self.instance.set(key, value, ttl=ttl, **kwargs)

    def get(self, key, default=None, **kwargs):
        return self.instance.get(key, default=default, **kwargs)

    def exists(self, key, **kwargs):
        return self.instance.exists(key, **kwargs)

    def incr(self, key, **kwargs):
        return self.instance.incr(key, **kwargs)
