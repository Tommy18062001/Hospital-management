# Generated by Django 3.1.3 on 2020-12-31 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0020_auto_20201230_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmodel',
            name='doctor_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]