# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (("entities", "0001_initial"),)

    def forwards(self, orm):
        # Adding model 'Template'
        db.create_table(u'sheets_template', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('uuid', self.gf('uuidfield.fields.UUIDField')(db_index=True, unique=True, max_length=32, blank=True)),
            ('period_start', self.gf('django.db.models.fields.DateField')(db_index=True, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('name_he', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(db_index=True, blank=True)),
            ('description_he', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_ar', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_ru', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'sheets', ['Template'])

        # Adding M2M table for field divisions on 'Template'
        m2m_table_name = db.shorten_name(u'sheets_template_divisions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('template', models.ForeignKey(orm[u'sheets.template'], null=False)),
            ('division', models.ForeignKey(orm[u'entities.division'], null=False))
        ))
        db.create_unique(m2m_table_name, ['template_id', 'division_id'])

        # Adding model 'TemplateNode'
        db.create_table(u'sheets_templatenode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('uuid', self.gf('uuidfield.fields.UUIDField')(db_index=True, unique=True, max_length=32, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('name_he', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('direction', self.gf('django.db.models.fields.CharField')(default='REVENUE', max_length=15, db_index=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['sheets.TemplateNode'])),
            ('path', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description_he', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sheets', ['TemplateNode'])

        # Adding M2M table for field inverse on 'TemplateNode'
        m2m_table_name = db.shorten_name(u'sheets_templatenode_inverse')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_templatenode', models.ForeignKey(orm[u'sheets.templatenode'], null=False)),
            ('to_templatenode', models.ForeignKey(orm[u'sheets.templatenode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_templatenode_id', 'to_templatenode_id'])

        # Adding M2M table for field backwards on 'TemplateNode'
        m2m_table_name = db.shorten_name(u'sheets_templatenode_backwards')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_templatenode', models.ForeignKey(orm[u'sheets.templatenode'], null=False)),
            ('to_templatenode', models.ForeignKey(orm[u'sheets.templatenode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_templatenode_id', 'to_templatenode_id'])

        # Adding model 'TemplateNodeRelation'
        db.create_table(u'sheets_templatenoderelation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sheets.Template'])),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sheets.TemplateNode'])),
        ))
        db.send_create_signal(u'sheets', ['TemplateNodeRelation'])

        # Adding unique constraint on 'TemplateNodeRelation', fields ['node', 'template']
        db.create_unique(u'sheets_templatenoderelation', ['node_id', 'template_id'])

        # Adding model 'Sheet'
        db.create_table(u'sheets_sheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('uuid', self.gf('uuidfield.fields.UUIDField')(db_index=True, unique=True, max_length=32, blank=True)),
            ('period_start', self.gf('django.db.models.fields.DateField')(db_index=True, null=True, blank=True)),
            ('period_end', self.gf('django.db.models.fields.DateField')(db_index=True, null=True, blank=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sheets', to=orm['entities.Entity'])),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(related_name='using_sheets', to=orm['sheets.Template'])),
            ('description', self.gf('django.db.models.fields.TextField')(db_index=True, blank=True)),
            ('description_he', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_ar', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_ru', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'sheets', ['Sheet'])

        # Adding model 'SheetItem'
        db.create_table(u'sheets_sheetitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('uuid', self.gf('uuidfield.fields.UUIDField')(db_index=True, unique=True, max_length=32, blank=True)),
            ('sheet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sheetitems', to=orm['sheets.Sheet'])),
            ('description', self.gf('django.db.models.fields.TextField')(db_index=True, blank=True)),
            ('description_he', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_ar', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_ru', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('budget', self.gf('django.db.models.fields.DecimalField')(db_index=True, null=True, max_digits=26, decimal_places=2, blank=True)),
            ('actual', self.gf('django.db.models.fields.DecimalField')(db_index=True, null=True, max_digits=26, decimal_places=2, blank=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sheetitems', to=orm['sheets.TemplateNode'])),
        ))
        db.send_create_signal(u'sheets', ['SheetItem'])

        # Adding model 'SheetItemComment'
        db.create_table(u'sheets_sheetitemcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('uuid', self.gf('uuidfield.fields.UUIDField')(db_index=True, unique=True, max_length=32, blank=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='discussion', to=orm['sheets.SheetItem'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_comments', to=orm['accounts.Account'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'sheets', ['SheetItemComment'])

        # Adding model 'DenormalizedSheetItem'
        db.create_table(u'sheets_denormalizedsheetitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('uuidfield.fields.UUIDField')(db_index=True, unique=True, max_length=32, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('name_he', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('direction', self.gf('django.db.models.fields.CharField')(default='REVENUE', max_length=15, db_index=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['sheets.DenormalizedSheetItem'])),
            ('path', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('sheet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denormalizedsheetitems', to=orm['sheets.Sheet'])),
            ('description', self.gf('django.db.models.fields.TextField')(db_index=True, blank=True)),
            ('description_he', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_ar', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('description_ru', self.gf('django.db.models.fields.TextField')(db_index=True, null=True, blank=True)),
            ('budget', self.gf('django.db.models.fields.DecimalField')(db_index=True, null=True, max_digits=26, decimal_places=2, blank=True)),
            ('actual', self.gf('django.db.models.fields.DecimalField')(db_index=True, null=True, max_digits=26, decimal_places=2, blank=True)),
            ('normal_item', self.gf('django.db.models.fields.related.OneToOneField')(related_name='denormalized', unique=True, to=orm['sheets.SheetItem'])),
            ('node_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('node_description_he', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('node_description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('node_description_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('node_description_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'sheets', ['DenormalizedSheetItem'])

        # Adding M2M table for field inverse on 'DenormalizedSheetItem'
        m2m_table_name = db.shorten_name(u'sheets_denormalizedsheetitem_inverse')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_denormalizedsheetitem', models.ForeignKey(orm[u'sheets.denormalizedsheetitem'], null=False)),
            ('to_denormalizedsheetitem', models.ForeignKey(orm[u'sheets.denormalizedsheetitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_denormalizedsheetitem_id', 'to_denormalizedsheetitem_id'])

        # Adding M2M table for field backwards on 'DenormalizedSheetItem'
        m2m_table_name = db.shorten_name(u'sheets_denormalizedsheetitem_backwards')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_denormalizedsheetitem', models.ForeignKey(orm[u'sheets.denormalizedsheetitem'], null=False)),
            ('to_denormalizedsheetitem', models.ForeignKey(orm[u'sheets.denormalizedsheetitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_denormalizedsheetitem_id', 'to_denormalizedsheetitem_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'TemplateNodeRelation', fields ['node', 'template']
        db.delete_unique(u'sheets_templatenoderelation', ['node_id', 'template_id'])

        # Deleting model 'Template'
        db.delete_table(u'sheets_template')

        # Removing M2M table for field divisions on 'Template'
        db.delete_table(db.shorten_name(u'sheets_template_divisions'))

        # Deleting model 'TemplateNode'
        db.delete_table(u'sheets_templatenode')

        # Removing M2M table for field inverse on 'TemplateNode'
        db.delete_table(db.shorten_name(u'sheets_templatenode_inverse'))

        # Removing M2M table for field backwards on 'TemplateNode'
        db.delete_table(db.shorten_name(u'sheets_templatenode_backwards'))

        # Deleting model 'TemplateNodeRelation'
        db.delete_table(u'sheets_templatenoderelation')

        # Deleting model 'Sheet'
        db.delete_table(u'sheets_sheet')

        # Deleting model 'SheetItem'
        db.delete_table(u'sheets_sheetitem')

        # Deleting model 'SheetItemComment'
        db.delete_table(u'sheets_sheetitemcomment')

        # Deleting model 'DenormalizedSheetItem'
        db.delete_table(u'sheets_denormalizedsheetitem')

        # Removing M2M table for field inverse on 'DenormalizedSheetItem'
        db.delete_table(db.shorten_name(u'sheets_denormalizedsheetitem_inverse'))

        # Removing M2M table for field backwards on 'DenormalizedSheetItem'
        db.delete_table(db.shorten_name(u'sheets_denormalizedsheetitem_backwards'))


    models = {
        u'accounts.account': {
            'Meta': {'ordering': "['email', 'created_on']", 'object_name': 'Account'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'he'", 'max_length': '2'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'entities.division': {
            'Meta': {'ordering': "['index', 'name']", 'unique_together': "(('name', 'domain'),)", 'object_name': 'Division'},
            'budgeting': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'divisions'", 'to': u"orm['entities.Domain']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'entities.domain': {
            'Meta': {'ordering': "['name']", 'object_name': 'Domain'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'usd'", 'max_length': '3'}),
            'ground_surface_unit': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'measurement_system': ('django.db.models.fields.CharField', [], {'default': "'metric'", 'max_length': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'entities.entity': {
            'Meta': {'ordering': "('division__domain', 'division__index', 'name')", 'unique_together': "(('name', 'parent', 'division'),)", 'object_name': 'Entity'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entities'", 'to': u"orm['entities.Division']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['entities.Entity']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'sheets.denormalizedsheetitem': {
            'Meta': {'ordering': "['code']", 'object_name': 'DenormalizedSheetItem'},
            'actual': ('django.db.models.fields.DecimalField', [], {'db_index': 'True', 'null': 'True', 'max_digits': '26', 'decimal_places': '2', 'blank': 'True'}),
            'backwards': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'forwards'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sheets.DenormalizedSheetItem']"}),
            'budget': ('django.db.models.fields.DecimalField', [], {'db_index': 'True', 'null': 'True', 'max_digits': '26', 'decimal_places': '2', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'blank': 'True'}),
            'description_ar': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'default': "'REVENUE'", 'max_length': '15', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inverse': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'inverse_rel_+'", 'null': 'True', 'to': u"orm['sheets.DenormalizedSheetItem']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'node_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'node_description_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'node_description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'node_description_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'node_description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'normal_item': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'denormalized'", 'unique': 'True', 'to': u"orm['sheets.SheetItem']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['sheets.DenormalizedSheetItem']"}),
            'path': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sheet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'denormalizedsheetitems'", 'to': u"orm['sheets.Sheet']"}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'sheets.sheet': {
            'Meta': {'ordering': "['entity']", 'object_name': 'Sheet'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'blank': 'True'}),
            'description_ar': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sheets'", 'to': u"orm['entities.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'period_end': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'period_start': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'using_sheets'", 'to': u"orm['sheets.Template']"}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'sheets.sheetitem': {
            'Meta': {'ordering': "['node']", 'object_name': 'SheetItem'},
            'actual': ('django.db.models.fields.DecimalField', [], {'db_index': 'True', 'null': 'True', 'max_digits': '26', 'decimal_places': '2', 'blank': 'True'}),
            'budget': ('django.db.models.fields.DecimalField', [], {'db_index': 'True', 'null': 'True', 'max_digits': '26', 'decimal_places': '2', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'blank': 'True'}),
            'description_ar': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sheetitems'", 'to': u"orm['sheets.TemplateNode']"}),
            'sheet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sheetitems'", 'to': u"orm['sheets.Sheet']"}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'sheets.sheetitemcomment': {
            'Meta': {'ordering': "['user', 'last_modified']", 'object_name': 'SheetItemComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'discussion'", 'to': u"orm['sheets.SheetItem']"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_comments'", 'to': u"orm['accounts.Account']"}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'sheets.template': {
            'Meta': {'ordering': "['name']", 'object_name': 'Template'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'blank': 'True'}),
            'description_ar': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'divisions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['entities.Division']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'period_start': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'sheets.templatenode': {
            'Meta': {'ordering': "['name']", 'object_name': 'TemplateNode'},
            'backwards': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'forwards'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sheets.TemplateNode']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'default': "'REVENUE'", 'max_length': '15', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inverse': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'inverse_rel_+'", 'null': 'True', 'to': u"orm['sheets.TemplateNode']"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['sheets.TemplateNode']"}),
            'path': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'templates': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'nodes'", 'symmetrical': 'False', 'through': u"orm['sheets.TemplateNodeRelation']", 'to': u"orm['sheets.Template']"}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'sheets.templatenoderelation': {
            'Meta': {'ordering': "['template__name', 'node__name']", 'unique_together': "(('node', 'template'),)", 'object_name': 'TemplateNodeRelation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sheets.TemplateNode']"}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sheets.Template']"})
        },
        u'sources.auxsource': {
            'Meta': {'ordering': "['last_modified', 'name']", 'object_name': 'AuxSource'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auxsources'", 'to': u"orm['accounts.Account']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'notes_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'retrieval_date': ('django.db.models.fields.DateField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'sources.referencesource': {
            'Meta': {'ordering': "['last_modified', 'name']", 'object_name': 'ReferenceSource'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referencesources'", 'to': u"orm['accounts.Account']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'notes_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'retrieval_date': ('django.db.models.fields.DateField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'})
        }
    }

    complete_apps = ['sheets']
