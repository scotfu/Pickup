#coding=utf8
from django.db import models

# Create your models here.


class Record(models.Model):
    incharge=models.CharField(u'接机负责人',max_length=100,default='',blank=True)
    name=models.CharField(u'姓名',max_length=100,default='',blank=True)
    flight_company=models.CharField(u'航空公司',max_length=100,default='',blank=True)
    flight_no=models.CharField(u'航班号',max_length=100,default='',blank=True)
    depart=models.DateTimeField(u'起飞时间')
    arrive=models.DateTimeField(u'到达时间')
    depart_airport=models.CharField(u'起飞机场',max_length=100,default='',blank=True)
    arrive_airport=models.CharField(u'到达机场',max_length=100,default='',blank=True)
    qq=models.CharField(u'QQ',max_length=100,default='',blank=True)
    email=models.EmailField(u'邮箱')
    phone=models.CharField(u'联系电话',max_length=100,default='',blank=True)
    package=models.CharField(u'行李数',max_length=100,default='',blank=True)
    need_room=models.BooleanField(u'需要住处')
    expect_district=models.CharField(u'预计找房地点',max_length=100,default='',blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'接机记录'
        verbose_name_plural = u'接机记录'



