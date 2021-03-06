# Generated by Django 2.2.10 on 2020-02-08 07:52

import common.baseModel
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
            ],
            bases=(models.Model, common.baseModel.BaseModel),
        ),
        migrations.AddField(
            model_name='item',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='item.category'),
            preserve_default=False,
        ),
    ]
