# Generated by Django 5.0.7 on 2024-07-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operator_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loadreport',
            name='operator',
        ),
        migrations.RemoveField(
            model_name='operator',
            name='avatar',
        ),
        migrations.AddField(
            model_name='operator',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='operator_photos/', verbose_name='عکس اپراتور'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='contact_number',
            field=models.CharField(max_length=200, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='delivered_device',
            field=models.CharField(max_length=200, verbose_name='دستگاه تحویلی'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='position',
            field=models.CharField(max_length=200, verbose_name='سمت'),
        ),
        migrations.DeleteModel(
            name='FailureReport',
        ),
        migrations.DeleteModel(
            name='LoadReport',
        ),
    ]
