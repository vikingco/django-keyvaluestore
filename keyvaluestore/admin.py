from django.contrib import admin

from keyvaluestore.models import KeyValueStore

class KeyValueStoreAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ('key', 'value')
admin.site.register(KeyValueStore, KeyValueStoreAdmin)