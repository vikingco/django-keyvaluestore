# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'KeyValueStore'
        db.create_table('keyvaluestore_keyvaluestore', (
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, primary_key=True, db_index=True)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('keyvaluestore', ['KeyValueStore'])


    def backwards(self, orm):
        
        # Deleting model 'KeyValueStore'
        db.delete_table('keyvaluestore_keyvaluestore')


    models = {
        'keyvaluestore.keyvaluestore': {
            'Meta': {'object_name': 'KeyValueStore'},
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['keyvaluestore']
