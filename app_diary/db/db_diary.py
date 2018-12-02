# -*- coding: utf-8 -*-
"""
 @Time    : 2018/8/19 0:20
 @Author  : CyanZoy
 @File    : db_diary.py
 @Describe: 应用app_diary 下数据库表 app_diary_diary
 """
from app_diary.models import *


class DbDiary:
    def __init__(self):
        pass

    @staticmethod
    def secelt_all():
        return Diary.objects.all().values()
