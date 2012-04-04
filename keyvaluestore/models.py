from django.db import models
from django.utils.translation import ugettext as _
from django.core.cache import cache

from keyvaluestore.managers import KeyValueStoreManager

class KeyValueStore(models.Model):
    key = models.CharField(max_length=200, primary_key=True, db_index=True, unique=True)
    value = models.TextField()

    objects = KeyValueStoreManager()

    class Meta:
        verbose_name = _('Key Value pair')
        verbose_name_plural = _('Key Value pairs')

    def __unicode__(self):
        return '%s: %s' % (self.key, self.value)

    def save(self, *args, **kwargs):
        self.key = self.key.upper()

        key = 'kvs_%s' % (self.key,)
        cache.delete(self.key)
        cache.set(self.key, self.value)

        super(KeyValueStore, self).save(*args, **kwargs)
