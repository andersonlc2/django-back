# Generated by Django 3.1.5 on 2021-01-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barb', '0003_auto_20210127_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
