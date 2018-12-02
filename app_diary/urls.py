# -*- coding: utf-8 -*-
"""
 @Time    : 2018/8/18 22:44
 @Author  : CyanZoy
 @File    : urls.py
 @Describe:
 """
from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', index),
    path('write', write),
    path('reward/search', search),
    path('reward/information', information),
    path('reward/save', save_information),
    url('detail/(.*)', detail),
    url('add_power', add_power),

]