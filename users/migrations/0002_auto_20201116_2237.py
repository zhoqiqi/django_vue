# Generated by Django 3.1.3 on 2020-11-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sp_user',
            name='qq_open_id',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='qq官方唯一编号信息'),
        ),
    ]