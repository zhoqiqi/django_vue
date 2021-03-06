# Generated by Django 3.1.3 on 2020-11-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('language', models.CharField(default='python', max_length=100)),
                ('style', models.CharField(default='friendly', max_length=100)),
            ],
            options={
                'db_table': 'snippet',
                'ordering': ['created'],
            },
        ),
    ]
