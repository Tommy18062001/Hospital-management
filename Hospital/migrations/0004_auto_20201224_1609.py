# Generated by Django 3.1.3 on 2020-12-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_auto_20201224_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormodel',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='doctormodel',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctormodel',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctormodel',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
