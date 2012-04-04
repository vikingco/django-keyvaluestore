from django.db import models
from django.core.cache import cache
from django.utils.translation import ugettext as _

from keyvaluestore.exceptions import KeyNotExistingException

class KeyValueStoreManager(models.Manager):
    def get_value_for_key(self, key):
        key = key.upper()
        cached = cache.get(key)

        if not cached:
            try:
                obj = self.get(key=key)
                cache.set('kvs_%s' % (key,), obj.value)

                return obj.value
            except:
                raise KeyNotExistingException(_(u"The request key '%s' could not be found." % (key,)))
        else:
            return cached