from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver # 导入receiver监听信号
from django.db.models.signals import post_save # 导入post_save信号
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class TempWork(models.Model):

    ticket_id = models.CharField(verbose_name="工单id", primary_key=True,max_length=200,default="111")
    #  该字段为主键
    process_recod = models.CharField('进度', max_length=2048)

class TempFlowIdRelation(models.Model):
    ticket_id =  models.CharField(verbose_name="工单id", primary_key=True,max_length=200,default="111")
    project_id = models.CharField(verbose_name="项目编号", max_length=200,default="等待指定")
# class ExtensionUser(models.Model):
#     """创建一对一模型，并添加新的字段"""
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     telephone = models.CharField(max_length=11,verbose_name="手机号码")
#
# @receiver(post_save,sender=User) # 监听到post_save事件且发送者是User则执行create_extension_user函数
# def create_extension_user(sender,instance,created,**kwargs):
#     """
#     sender:发送者
#     instance:save对象
#     created:是否是创建数据
#     """
#     if created:
#         # 如果创建对象，ExtensionUser进行绑定
#         ExtensionUser.objects.create(user=instance)
#     else:
#         # 如果不是创建对象，同样将改变进行保存
#         instance.extension.save()

