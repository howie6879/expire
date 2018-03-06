#!/usr/bin/env python
"""
Tips for human caches: there are several simple caching schemes we provide for you, and you can use the following ways.
    - Use RedisCache,MemcachedCache,MemoryCache class directly
    - Use cached decorator
"""
from expire import Settings
from expire import RedisCache, cached, CacheSetting


class MySettings(Settings):
    """
    Create custom configuration
    """
    cache = {
        'cache_class': RedisCache,
        'cache_config': {
            'host': '127.0.0.1',
            'port': 6379,
            'db': 0,
            'password': None
        },
        'serializer': None
    }


@cached(**MySettings.cache, ttl=1000)
def parse(url, params=None, **kwargs):
    return "{0}: {1}".format(url, 'hello')


def cached_by_redis(key):
    cache_ins = CacheSetting(MySettings)
    return cache_ins.get(key)


if __name__ == '__main__':
    key = 'expire'
    # Set
    result = parse(url=key, dynamic_key=key)
    print(result)
    # Get
    print(cached_by_redis(key))
