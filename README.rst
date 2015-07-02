===================================
A simple key-value-store for Django
===================================

django-keyvaluestore implements a very simple database-based key-value store for Django.

Usage
=====
The interface is straightforward::

  from keyvaluestore import get_value_for_key, set_key_value
  set_key_value('foo', 'bar')
  get_value_for_key('foo')
