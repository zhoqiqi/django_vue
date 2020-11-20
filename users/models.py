from django.db import models

# Create your models here.
'''
CREATE TABLE `sp_user` (
  `user_id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `username` varchar(128) NOT NULL DEFAULT '' COMMENT '登录名',
  `qq_open_id` char(32) DEFAULT NULL COMMENT 'qq官方唯一编号信息',
  `password` char(64) NOT NULL DEFAULT '' COMMENT '登录密码',
  `user_email` varchar(64) NOT NULL DEFAULT '' COMMENT '邮箱',
  `user_email_code` char(13) DEFAULT NULL COMMENT '新用户注册邮件激活唯一校验码',
  `is_active` enum('是','否') DEFAULT '否' COMMENT '新用户是否已经通过邮箱激活帐号',
  `user_sex` enum('保密','女','男') NOT NULL DEFAULT '男' COMMENT '性别',
  `user_qq` varchar(32) NOT NULL DEFAULT '' COMMENT 'qq',
  `user_tel` varchar(32) NOT NULL DEFAULT '' COMMENT '手机',
  `user_xueli` enum('博士','硕士','本科','专科','高中','初中','小学') NOT NULL DEFAULT '本科' COMMENT '学历',
  `user_hobby` varchar(32) NOT NULL DEFAULT '' COMMENT '爱好',
  `user_introduce` text COMMENT '简介',
  `create_time` int NOT NULL COMMENT '创建时间',
  `update_time` int NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='会员表';
'''


class Sp_user(models.Model):
    ACTION_CHOICE = (
        ('是', '是'),
        ('否', '否')
    )
    SEX_CHOICE = (
        ('保密', '保密'),
        ('男', '男'),
        ('女', '女')
    )
    XUELI_CHOICE = (
        ('博士', '博士'),
        ('硕士', '硕士'),
        ('本科', '本科'),
        ('专科', '专科'),
        ('高中', '高中'),
        ('初中', '初中'),
        ('小学', '小学'),
    )
    user_id = models.IntegerField(primary_key=True, auto_created=True, verbose_name='自增id')
    username = models.CharField(max_length=128, default='', verbose_name='登录名')
    qq_open_id = models.CharField(max_length=32, null=True, blank=True, verbose_name='qq官方唯一编号信息')
    password = models.CharField(max_length=64, default='', verbose_name='登录密码')
    user_email = models.CharField(max_length=64, default='', verbose_name='邮箱')
    user_email_code = models.CharField(max_length=13, null=True, blank=True, verbose_name='新用户注册邮件激活唯一校验码')
    is_active = models.CharField(choices=ACTION_CHOICE, default='否', max_length=32, verbose_name='新用户是否已经通过邮箱激活帐号')
    user_sex = models.CharField(choices=SEX_CHOICE, default='男', max_length=32, verbose_name='性别')
    user_qq = models.CharField(max_length=32, default='', verbose_name='qq')
    user_tel = models.CharField(max_length=32, default='', verbose_name='手机')
    user_xueli = models.CharField(choices=XUELI_CHOICE, default='本科', max_length=32, verbose_name='学历')
    user_hobby = models.CharField(max_length=32, default='', verbose_name='爱好')
    user_introduce = models.TextField(verbose_name='简历', null=True)
    create_time = models.IntegerField(verbose_name='创建时间')
    update_time = models.IntegerField(verbose_name='修改时间')

    class Meta:
        db_table = 'sp_user'  # 指明数据库表名
        verbose_name = '会员表'  # 在admin站点中显示的名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.username
