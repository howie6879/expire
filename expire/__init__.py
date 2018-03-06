from .cache_setting import CacheSetting
from .decorator import cached
from .memcached_cache import MemcachedCache
from .memory_cache import MemoryCache
from .redis_cache import RedisCache
from .serializer import JsonSerializer, PickleSerializer, StrSerializer


class Settings:
    """Global Settings"""
    cache = {
        'cache_class': MemoryCache,
        'cache_config': {},
        'serializer': None,
        'ttl': None
    }
