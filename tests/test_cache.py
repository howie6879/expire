#!/usr/bin/env python
from expire import CacheSetting, JsonSerializer, MemoryCache, PickleSerializer, Settings, cached


def test_memory_cache():
    memory_cache = MemoryCache()
    memory_cache.set('name', 'expire')
    cache_ins = CacheSetting()
    assert cache_ins.get('name') == 'expire'


def test_cached():
    cache_ins = CacheSetting(Settings)

    @cached(**Settings.cache)
    def hello_cache(name, **kwargs):
        return 'hello expire'

    name = 'expire'
    hello_cache(name=name, dynamic_key=name)
    assert cache_ins.get(name) == 'hello expire'


def test_serializer():
    test = {
        'name': 'expire',
        'url': 'https://github.com/howie6879/expire'
    }
    serializer_ins = JsonSerializer()
    pickle_ins = PickleSerializer()
    assert pickle_ins.loads(pickle_ins.dumps(test)) == test
    assert serializer_ins.loads(serializer_ins.dumps(test)) == test
