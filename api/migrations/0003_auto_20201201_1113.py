# Generated by Django 3.1.3 on 2020-12-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_productinfo_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinfo',
            name='bought',
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='price',
            field=models.CharField(max_length=5),
        ),
    ]
