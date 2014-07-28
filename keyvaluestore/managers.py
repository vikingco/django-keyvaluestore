from django.db import models
from django.core.cache import cache
from django.utils.translation import ugettext as _

class KeyValueStoreManager(models.Manager):
    def get_value_for_key(self, key):
        key = key.upper()
        cached_key = 'kvs_%s' % (key,)
        cached = cache.get(cached_key)

        if not cached:
            try:
                obj = self.get(key=key)
                cache.set(cached_key, obj.value)

                return obj.value
            except:
                raise KeyError(_(u"The request key '%s' could not be found." % (key,)))
        else:
            return cached
