# Generated by Django 3.1.3 on 2020-12-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0015_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
