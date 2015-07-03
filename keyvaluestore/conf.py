from django.conf import settings

# Use Django cache to prevent multiple database hits
ENABLE_CACHING = getattr(settings, 'KEYVALUESTORE_CACHING', True)

# Use this prefix if caching is enabled
# Cache keys will be constructed like '%s%s' % (CACHE_PREFIX, key)
CACHE_PREFIX = getattr(settings, 'KEYVALUESTORE_CACHE_PREFIX', 'kvs_')

# The timeout for the cache if it's enabled (in seconds)
CACHE_TIMEOUT = getattr(settings, 'KEYVALUESTORE_CACHE_TIMEOUT', None)
