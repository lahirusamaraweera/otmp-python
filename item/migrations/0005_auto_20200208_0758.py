# Generated by Django 2.2.10 on 2020-02-08 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20200208_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='category_id',
            new_name='category',
        ),
    ]