# Generated by Django 3.1.3 on 2020-12-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0002_doctormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormodel',
            name='user_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
