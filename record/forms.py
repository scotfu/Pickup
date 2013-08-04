#coding=utf-8
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django import forms
import re


class RecordForm(forms.Form):
    name=forms.CharField(label=u'姓名',max_length=100)
    flight_company=forms.CharField(label=u'航空公司',max_length=100)
    flight_no=forms.CharField(label=u'航班号',max_length=100)
    depart=forms.DateTimeField(label=u'起飞时间',widget=forms.TextInput(attrs={'data-format':'yyyy-MM-dd hh:mm:ss','tip':'当地时间'}))
    arrive=forms.DateTimeField(label=u'到达时间',widget=forms.TextInput(attrs={'data-format':'yyyy-MM-dd hh:mm:ss','tip':'当地时间'}))
    depart_airport=forms.CharField(label=u'起飞机场')
    arrive_airport=forms.CharField(label=u'到达机场')
    qq=forms.CharField(label=u'QQ',max_length=100)
    email=forms.EmailField(label=u'邮箱',required=False)
    phone=forms.CharField(label=u'联系电话',required=False)
    package=forms.CharField(label=u'行李数',required=False)
    need_room=forms.BooleanField(label=u'是否需要住处',required=False)
    expect_district=forms.CharField(label=u'预计找房地点',required=False)


    def clean_name(self):
        name=self.cleaned_data['name']
        if name=='':
            raise ValidationError(u'少年，名字要填一下啊')
        return name

    def clean_flight_company(self):
        flight_company=self.cleaned_data['flight_company']
        return flight_company

    def clean_flight_no(self):
        flight_no=self.cleaned_data['flight_no']
        return flight_no

    def clean_depart(self):
        depart=self.cleaned_data['depart']
        return depart

    def clean_arrive(self):
        arrive=self.cleaned_data['arrive']
        return arrive

    def clean_depart_airport(self):
        depart_airport=self.cleaned_data['depart_airport']
        return depart_airport

    def clean_arrive_airport(self):
        arrive_airport=self.cleaned_data['arrive_airport']
        return arrive_airport

    def clean_qq(self):
        qq=self.cleaned_data['qq']
        return qq

    def clean_email(self):
        email=self.cleaned_data['email']
        return email

    def clean_phone(self):
        phone=self.cleaned_data['phone']
        return phone

    def clean_package(self):
        package=self.cleaned_data['package']
        return package

    def clean_need_room(self):
        need_room=self.cleaned_data['need_room']
        return need_room

    def clean_expect_district(self):
        expect_district=self.cleaned_data['expect_district']
        return expect_district
