# Generated by Django 4.1.5 on 2023-01-27 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_checkin_sickness_alter_medicine_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='checkin',
        ),
        migrations.RemoveField(
            model_name='orderloan',
            name='checkin',
        ),
        migrations.DeleteModel(
            name='Checkin',
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='OrderLoan',
        ),
    ]
