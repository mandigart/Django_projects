
from __future__ import unicode_literals
from django.db import migrations, models
import django_extensions.db.fields
import waterMark.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id',          models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created',     django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified',    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title',       models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image',       models.ImageField(upload_to=waterMark.models.image_upload_to, verbose_name='original image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
