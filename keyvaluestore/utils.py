from keyvaluestore.models import KeyValueStore

def get_value_for_key(key):
    return KeyValueStore.objects.get_value_for_key(key)

def set_key_value(key, value):
    obj,created = KeyValueStore.objects.get_or_create(key=key, value=value)
    if not created:
        obj.value = value
        obj.save()
    return True