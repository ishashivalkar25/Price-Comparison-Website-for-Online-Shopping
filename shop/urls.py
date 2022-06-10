# -*- coding: utf-8 -*-
"""
Created on Sun May 29 09:58:06 2022

@author: Rutuja Patil
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome")
]