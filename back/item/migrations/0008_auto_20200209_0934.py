# Generated by Django 2.2.10 on 2020-02-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_auto_20200209_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='qty',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]