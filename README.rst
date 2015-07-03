===================================
A simple key-value-store for Django
===================================
django-keyvaluestore implements a very simple database-based key-value store for Django.

Usage
=====
The interface is straightforward::

  from keyvaluestore import KeyValueStore

  KeyValueStore.set('foo', 'bar')

  KeyValueStore.get('foo')
   >> 'bar'

  KeyValueStore.get('zork', 'fallback')
   >> 'fallback'

  KeyValueStore.get('zork')
    KeyError("No value exists for key 'zork'")

Configuration
=============
By default the KeyValueStore will use Django's cache system to prevent multiple database lookups. This behavior can
be modified with the following settings:

KEYVALUESTORE_CACHING
  Enable or disable the caching entirely. Defaults to True.

KEYVALUESTORE_CACHE_PREFIX
  The prefix used for the cache keys. Defaults to 'kvs\_'.

KEYVALUESTORE_CACHE_TIMEOUT
  The timeout for the cache values. Defaults to None (key-value pairs are cached infinitely).
