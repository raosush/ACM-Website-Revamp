# Generated by Django 2.0 on 2020-03-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMP', '0003_auto_20191209_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smp',
            name='mentors',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='smp',
            name='name',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='smp',
            name='overview',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='smp',
            name='platform_of_tutoring',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='smp_des',
            name='sub_des',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='smp_des',
            name='sub_heading',
            field=models.CharField(max_length=20000),
        ),
    ]
