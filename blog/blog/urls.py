# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 09:52:34 2022

@author: sac13
"""

from django.urls import path 
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, En_vivo
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/',BlogDetailView.as_view(), name='post_detail'),
    path('',BlogListView.as_view(),name='home'),
    path('En_vivo/',En_vivo.as_view(), name='Envivo'),
    ]
urlpatterns += staticfiles_urlpatterns()

