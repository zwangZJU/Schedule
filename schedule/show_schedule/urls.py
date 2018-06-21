# -*- coding: utf-8 -*-
'''
@Author: wzlab
@Date  : 2018/5/14
@Desc  : 
'''
from django.urls import path
from . import views
urlpatterns = [

    path('',views.index),
    path('week/',views.week),
    path('plan_details/',views.plan_detail),

    path('week/<int:week_number>',views.find_plan_by_week),
]