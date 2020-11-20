# Generated by Django 3.1.3 on 2020-11-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sp_user',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='自增id')),
                ('username', models.CharField(default='', max_length=128, verbose_name='登录名')),
                ('qq_open_id', models.CharField(default='', max_length=32, verbose_name='qq官方唯一编号信息')),
                ('password', models.CharField(default='', max_length=64, verbose_name='登录密码')),
                ('user_email', models.CharField(default='', max_length=64, verbose_name='邮箱')),
                ('user_email_code', models.CharField(blank=True, max_length=13, null=True, verbose_name='新用户注册邮件激活唯一校验码')),
                ('is_active', models.CharField(choices=[('是', '是'), ('否', '否')], default='否', max_length=32, verbose_name='新用户是否已经通过邮箱激活帐号')),
                ('user_sex', models.CharField(choices=[('保密', '保密'), ('男', '男'), ('女', '女')], default='男', max_length=32, verbose_name='性别')),
                ('user_qq', models.CharField(default='', max_length=32, verbose_name='qq')),
                ('user_tel', models.CharField(default='', max_length=32, verbose_name='手机')),
                ('user_xueli', models.CharField(choices=[('博士', '博士'), ('硕士', '硕士'), ('本科', '本科'), ('专科', '专科'), ('高中', '高中'), ('初中', '初中'), ('小学', '小学')], default='本科', max_length=32, verbose_name='学历')),
                ('user_hobby', models.CharField(default='', max_length=32, verbose_name='爱好')),
                ('user_introduce', models.TextField(verbose_name='简历')),
                ('create_time', models.IntegerField(verbose_name='创建时间')),
                ('update_time', models.IntegerField(verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '会员表',
                'db_table': 'sp_user',
            },
        ),
    ]
