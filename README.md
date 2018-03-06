# Expire

![PyPI](https://img.shields.io/pypi/v/expire.svg)

## What is Expire

When you are writing a service, maybe you need to be able to save a piece of JSON data to your system's memory.

Expire aims to make using cache as convenient as possible.

There are three ways to create a cache, which are MemoryCache, RedisCache or MemcachedCache.

## How to Use?

### Installation

**Run:**

``` shell
pip install expire

pip install git+https://github.com/howie6879/expire.git
```

### Usage

**MemoryCache:** easy to configure, but it automatically destroys when the server is stopped.

``` python
from expire import CacheSetting, MemoryCache

memory_cache = MemoryCache()
memory_cache.set('name', 'expire')
cache_ins = CacheSetting()
print(cache_ins.get('name'))

# Output: expire
```

**RedisCache:** stable but you have to install Redis.

``` python
from expire import Settings
from expire import RedisCache, cached, CacheSetting

class MySettings(Settings):
    """
    Create custom configuration
    """
    cache = {
        # RedisCache, MemoryCache or MemcachedCache
        'cache_class': RedisCache,
        'cache_config': {
            'host': '127.0.0.1',
            'port': 6379,
            'db': 0,
            'password': None
        },
        # JsonSerializer, PickleSerializer or StrSerializer
        'serializer': None
    }
@cached(**MySettings.cache, ttl=1000)
def parse(url, params=None, **kwargs):
    return "{0}: {1}".format(url, 'hello')


def cached_by_redis(key):
    cache_ins = CacheSetting(MySettings)
    return cache_ins.get(key)

key = 'expire'
result = parse(url=key, dynamic_key=key)
print(result)
# Output 'expire: hello'
print(cached_by_redis(key))
# Output 'expire: hello'
```