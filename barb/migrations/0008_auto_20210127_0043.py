# Generated by Django 3.1.5 on 2021-01-27 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barb', '0007_barber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='beard',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='services',
            name='hair',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='services',
            name='sealing',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Scheduling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.DateTimeField(verbose_name='hour of scheduling')),
                ('serviceHair', models.BooleanField(default=False)),
                ('serviceBeard', models.BooleanField(default=False)),
                ('serviceSealing', models.BooleanField(default=False)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barb.barber')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barb.client')),
            ],
        ),
    ]
