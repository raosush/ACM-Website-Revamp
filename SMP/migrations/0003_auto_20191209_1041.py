# Generated by Django 2.2.7 on 2019-12-09 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SMP', '0002_auto_20191209_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smp',
            name='head_contact_number',
        ),
        migrations.RemoveField(
            model_name='smp',
            name='head_name',
        ),
    ]
