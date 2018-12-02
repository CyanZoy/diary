# -*- coding: utf-8 -*-
"""
 @Time    : 2018/12/1 10:22
 @Author  : CyanZoy
 @File    : urls.py
 @Software: PyCharm
 """
from django.conf import urls
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index)
]