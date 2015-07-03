from django.db import models
from django.core.cache import cache

from .conf import ENABLE_CACHING, CACHE_PREFIX, CACHE_TIMEOUT

class KeyValueStore(models.Model):
    key = models.CharField(max_length=200, primary_key=True, db_index=True, unique=True)
    value = models.TextField()

    class Meta:
        verbose_name = u'Key Value pair'
        verbose_name_plural = u'Key Value pairs'

    def __unicode__(self):
        return '%s: %s' % (self.key, self.value)

    def __repr__(self):
        return 'KeyValueStore(key="%s", value="%s")' % (self.key, self.value)


    @classmethod
    def _get_cache_key(cls, key):
        """
        Construct a cache key for a key.
        """
        return '%s%s' % (CACHE_PREFIX, key)


    def save(self, *args, **kwargs):
        # If caching is enabled, cache the key-value pair
        if ENABLE_CACHING:
            cache_key = KeyValueStore._get_cache_key(self.key)
            cache.set(cache_key, self.value, CACHE_TIMEOUT)

        super(KeyValueStore, self).save(*args, **kwargs)


    @classmethod
    def get(cls, key, default=None):
        """
        Retrieve a value from the store.

        If caching is enabled, first the cache will be checked. If it's empty, the key-value pair will be cached.
        If the default parameter is provided, an invalid key will return the default. Otherwise a KeyError will
        be raised.
        """
        try:
            if ENABLE_CACHING:
                cache_key = cls._get_cache_key(key)
                cached = cache.get(cache_key)
                if cached:
                    return cached
                else:
                    value = cls.objects.get(key=key)
                    cache.set(cache_key, value)
                    return value
            else:
                return cls.objects.get(key=key)
        except KeyValueStore.DoesNotExist:
            if default is not None:
                return default
            else:
                raise KeyError('No value exists for key %s' % key)


    @classmethod
    def set(cls, key, value):
        """
        Set a key-value pair in the store.
        """
        obj, created = KeyValueStore.objects.get_or_create(key=key, defaults={'value': value})
        if not created:
            obj.value = value
            obj.save()
